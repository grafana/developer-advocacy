#!/bin/bash

# Wrapper script to run the complete tabs-or-spaces analysis workflow
# This script:
# 1. Clones or pulls the Github-Ranking repository
# 2. Runs fetch_repos.sh to get the repositories
# 3. Runs tabsorspaces.py to analyze the repositories

set -e  # Exit on any error

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

echo_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

echo_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Step 1: Clone or pull Github-Ranking repository
echo_info "Step 1: Setting up Github-Ranking repository..."

GITHUB_RANKING_DIR="$SCRIPT_DIR/Github-Ranking"
GITHUB_RANKING_URL="https://github.com/EvanLi/Github-Ranking.git"

if [ -d "$GITHUB_RANKING_DIR" ]; then
    echo_info "Github-Ranking directory exists, pulling latest changes..."
    cd "$GITHUB_RANKING_DIR"
    if ! git pull; then
        echo_error "Failed to pull Github-Ranking repository"
        exit 1
    fi
    cd "$SCRIPT_DIR"
else
    echo_info "Cloning Github-Ranking repository..."
    if ! git clone "$GITHUB_RANKING_URL" "$GITHUB_RANKING_DIR"; then
        echo_error "Failed to clone Github-Ranking repository"
        exit 1
    fi
fi

echo_info "Github-Ranking repository is up to date."

# Step 2: Create evaluated_projects directory and run fetch_repos.sh
echo_info "Step 2: Setting up evaluated_projects directory..."

EVALUATED_PROJECTS_DIR="$SCRIPT_DIR/evaluated_projects"
if [ ! -d "$EVALUATED_PROJECTS_DIR" ]; then
    echo_info "Creating evaluated_projects directory..."
    mkdir -p "$EVALUATED_PROJECTS_DIR"
fi

echo_info "Running fetch_repos.sh to fetch repositories..."
if ! bash "$SCRIPT_DIR/fetch_repos.sh"; then
    echo_error "fetch_repos.sh failed"
    exit 1
fi

echo_info "Repositories fetched successfully."

# Step 3: Run tabsorspaces.py analysis
echo_info "Step 3: Running tabsorspaces.py analysis..."

# Temporarily disable exit on error so we can continue processing other repos
# even if one fails
set +e

# Find all code files in evaluated_projects and analyze them
# We'll process each repository owner/repo combination
for owner_dir in "$EVALUATED_PROJECTS_DIR"/*; do
    if [ ! -d "$owner_dir" ]; then
        continue
    fi
    
    owner=$(basename "$owner_dir")
    
    for repo_dir in "$owner_dir"/*; do
        if [ ! -d "$repo_dir" ]; then
            continue
        fi
        
        repo=$(basename "$repo_dir")
        
        echo_info "Analyzing $owner/$repo..."
        
        # Find code files using is_code.sh
        code_files=$(bash "$SCRIPT_DIR/is_code.sh" "$repo_dir")
        
        if [ -z "$code_files" ]; then
            echo_warn "No code files found in $owner/$repo, skipping..."
            continue
        fi
        
        # Run tabsorspaces.py with the code files
        echo "$code_files" | python3 "$SCRIPT_DIR/tabsorspaces.py" \
            --repo-owner "$owner" \
            --repo-name "$repo" \
            --csv
        
        if [ $? -ne 0 ]; then
            echo_error "Failed to analyze $owner/$repo"
            # Continue with other repos instead of exiting
        fi
    done
done

# Re-enable exit on error
set -e

echo_info "Analysis complete!"

