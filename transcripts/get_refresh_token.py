"""One-time helper: sign in as a YouTube channel manager and print an OAuth refresh token.

The scheduled transcript run downloads captions with the official YouTube API, which needs the
permission of someone who can edit the videos. This script runs the normal Google sign-in in your
browser and prints a refresh token. Give that token to whoever stores the secrets (Vault, see
README.md); do not commit it, paste it into an issue, or put it in a GitHub Actions secret.

Usage (standard library only, no virtual environment needed):

    python3 get_refresh_token.py

It asks for the OAuth client ID and secret (or reads YOUTUBE_OAUTH_CLIENT_ID and
YOUTUBE_OAUTH_CLIENT_SECRET) of a "Desktop app" OAuth client, opens your browser, listens on
127.0.0.1 for Google's redirect, and prints the refresh token to the terminal only.
"""
import base64
import getpass
import hashlib
import http.server
import json
import os
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
TIMEOUT_SECONDS = 300


def pkce_pair():
    """A PKCE (code_verifier, code_challenge) pair, S256."""
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    return verifier, challenge


def build_auth_url(client_id, redirect_uri, state, challenge):
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": SCOPE,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        # offline + consent make Google return a refresh token even if you signed in before.
        "access_type": "offline",
        "prompt": "consent",
    }
    return f"{AUTH_URI}?{urllib.parse.urlencode(params)}"


def exchange_code(client_id, client_secret, code, verifier, redirect_uri):
    data = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "code_verifier": verifier,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
    }).encode()
    request = urllib.request.Request(TOKEN_URI, data=data)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        sys.exit(f"Google refused the sign-in: {error.read().decode(errors='replace')}")


def wait_for_redirect(server):
    """Serve one redirect from Google and return its query parameters."""
    result = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if "code" in query or "error" in query:
                result.update({k: v[0] for k, v in query.items()})
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"You can close this tab and return to the terminal.")

        def log_message(self, *args):
            pass

    server.RequestHandlerClass = Handler
    server.timeout = 5
    deadline = time.monotonic() + TIMEOUT_SECONDS
    while not result and time.monotonic() < deadline:
        server.handle_request()
    return result


def main():
    client_id = os.environ.get("YOUTUBE_OAUTH_CLIENT_ID") or input("OAuth client ID: ").strip()
    client_secret = os.environ.get("YOUTUBE_OAUTH_CLIENT_SECRET") or getpass.getpass("OAuth client secret (hidden): ").strip()
    if not client_id or not client_secret:
        sys.exit("A client ID and secret are required.")

    server = http.server.HTTPServer(("127.0.0.1", 0), http.server.BaseHTTPRequestHandler)
    redirect_uri = f"http://127.0.0.1:{server.server_port}"
    verifier, challenge = pkce_pair()
    state = secrets.token_urlsafe(16)
    url = build_auth_url(client_id, redirect_uri, state, challenge)

    print("Opening your browser. Sign in with the Google account that manages the YouTube channel")
    print("(the one that can edit the videos), and approve access to YouTube captions.")
    print(f"If it does not open, visit:\n\n{url}\n")
    webbrowser.open(url)

    result = wait_for_redirect(server)
    server.server_close()
    if not result:
        sys.exit("Timed out waiting for the sign-in. Run the script again.")
    if "error" in result:
        sys.exit(f"Sign-in failed: {result['error']}")
    if result.get("state") != state:
        sys.exit("Sign-in failed: the response did not match this request (state mismatch).")

    tokens = exchange_code(client_id, client_secret, result["code"], verifier, redirect_uri)
    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        sys.exit("Google did not return a refresh token. Remove this app at "
                 "https://myaccount.google.com/permissions and run the script again.")

    print("\nRefresh token (store it in Vault; do not commit it or paste it in chat or an issue):\n")
    print(refresh_token)
    print("\nNothing was written to disk.")


if __name__ == "__main__":
    main()
