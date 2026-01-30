#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SRCDIR="${SCRIPT_DIR}/evaluated_projects"
TOP100DIR="${SCRIPT_DIR}/Github-Ranking/Data"

cd "$TOP100DIR"
git pull
if [ $? -ne 0 ]
then
    # TODO: Log an error
    echo "Error pulling Top 100"
    exit 1
else
    LATEST=$(ls -1 | tail -1)
    # Get the directory names for each repo
    mapfile -t REPO_NAMES < <(awk -F',' 'NR > 1 { print $3 }' "$LATEST" | head -100)
    # Get the URL for each repo
    mapfile -t REPO_URLS < <(awk -F',' 'NR > 1 { print $7 }' "$LATEST" | head -100)
    # Get the GitHub repo name for each repo
    #mapfile -t < GH_REPOS <(awk -F',' 'NR > 1 { print $8"/"$3 }' "$LATEST" | head -100)
fi

cd "$SRCDIR"

# Function to extract owner/repo path from GitHub URL
# e.g., "https://github.com/codecrafters-io/build-your-own-x" -> "codecrafters-io/build-your-own-x"
extract_repo_path() {
    local url="$1"
    # Remove https://github.com/ or http://github.com/ prefix
    local path="${url#https://github.com/}"
    path="${path#http://github.com/}"
    # Remove .git suffix if present
    path="${path%.git}"
    echo "$path"
}

# Track expected repository paths
declare -A EXPECTED_REPOS

ARRLEN=${#REPO_NAMES[@]}
for (( i=0; i<$ARRLEN; i++ ))
do
    echo "Fetching ${REPO_NAMES[$i]}..."
    cur="${REPO_NAMES[$i]}"
    repo_path=$(extract_repo_path "${REPO_URLS[$i]}")
    EXPECTED_REPOS["$repo_path"]=1
    
    # Extract owner and repo name from path
    owner=$(dirname "$repo_path")
    repo=$(basename "$repo_path")
    
    # Create owner directory if it doesn't exist
    if [ ! -d "$owner" ]
    then
        mkdir -p "$owner"
    fi
    
    # Check if repo exists in the nested structure
    if [ -d "$repo_path" ]
    then
        # Repo already exists; just update
        cd "$repo_path"
        git pull
        if [ $? -ne 0 ]
        then
            #TODO: Log an error
            echo "Error pulling $repo_path from GitHub"
        fi
        cd "$SRCDIR"
    else
        # Repo doesn't already exist; clone it into the nested structure
        cd "$owner"
        git clone "${REPO_URLS[$i]}" "$repo"
        if [ $? -ne 0 ]
        then
            #TODO: Log an error
            echo "Error cloning $repo_path from GitHub"
        fi
        cd "$SRCDIR"
    fi

    sleep 30    # Try not to get rate limited; note that this will make this script take a long time to run!
done

# Remove repositories that are no longer in the list
echo "Checking for repositories to remove..."
for owner_dir in "$SRCDIR"/*; do
    if [ -d "$owner_dir" ] && [ "$(basename "$owner_dir")" != "." ] && [ "$(basename "$owner_dir")" != ".." ]; then
        owner_name=$(basename "$owner_dir")
        for repo_dir in "$owner_dir"/*; do
            if [ -d "$repo_dir" ]; then
                repo_name=$(basename "$repo_dir")
                repo_path="$owner_name/$repo_name"
                if [ ! -v EXPECTED_REPOS["$repo_path"] ]; then
                    echo "Removing old repository: $repo_path"
                    rm -rf "$repo_dir"
                fi
            fi
        done
        # Remove owner directory if it's now empty
        if [ -z "$(ls -A "$owner_dir")" ]; then
            echo "Removing empty owner directory: $owner_name"
            rmdir "$owner_dir"
        fi
    fi
done
