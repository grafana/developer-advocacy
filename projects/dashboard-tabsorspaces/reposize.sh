#!/bin/bash

# Point this at the directory containing the GH star data (Github-Ranking/Data)

LATEST=$(ls -1 $1/github-ranking* | tail -1)
REPOS=$(awk -F',' 'NR > 1 { print $8"/"$3 }' "$LATEST" | head -100)

mapfile -t FORMATTED_REPOS <<< "$REPOS"

echo -e "Repo\tSize"
for i in "${FORMATTED_REPOS[@]}"
do
  echo -en "$i\t"
  curl -s "https://api.github.com/repos/$i" | jq '.size'
done