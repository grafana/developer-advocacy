# YouTube Transcripts

This directory contains a small script which fetches transcripts from the YouTube API, so that we can have
a separate repo of text/markdown corresponding to all of the content in the videos we produce.  

## Setup

* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`

## Configure Environment

Edit `.env` file and set `API_KEY` to the correct value.

## Need a Key?

* Go to a GCP project, make sure YouTube Data API v3 is enabled
* Create an API key in that project and use that for this value.

