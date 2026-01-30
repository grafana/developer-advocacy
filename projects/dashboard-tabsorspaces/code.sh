#!/bin/bash

# Usage: ./detect_code.sh /path/to/folder

if [ $# -ne 1 ]; then
    echo "Usage: $0 <folder_to_scan>"
    exit 1
fi

SCAN_DIR="$1"

# List of MIME types considered as code
code_mimes=(
    "text/x-python"
    "text/x-c"
    "text/x-c++"
    "text/x-java-source"
    "text/x-shellscript"
    "text/x-ruby"
    "text/x-go"
    "text/x-php"
    "text/x-rust"
    "text/x-typescript"
    "text/x-csharp"
    "text/x-swift"
    "text/x-kotlin"
    "text/x-perl"
    "text/x-sql"
    "text/x-dockerfile"
    "text/x-makefile"
    "text/plain"
)

# Function to check if a MIME type is in the list
is_code_mime() {
    local mime="$1"
    for cmime in "${code_mimes[@]}"; do
        if [[ "$mime" == "$cmime" ]]; then
            return 0
        fi
    done
    return 1
}

# Recursively scan files
find "$SCAN_DIR" -type f | while read -r file; do
    # Skip empty files
    [ ! -s "$file" ] && continue

    # Get MIME type
    mime=$(file --mime-type -b "$file")

    # Skip obvious binary files
    if [[ $mime != text/* ]]; then
        continue
    fi

    # Check if MIME type matches code
    if is_code_mime "$mime"; then
        echo "$file"
    fi
done
