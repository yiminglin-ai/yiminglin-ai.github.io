#!/bin/bash

# Deploy script for Life in the UK App
# Copies relevant files from master to gh-pages/life-in-the-uk

# Ensure we are on master
if [[ $(git rev-parse --abbrev-ref HEAD) != "master" ]]; then
  echo "Error: You must be on the master branch to run this script."
  exit 1
fi

# Check for uncommitted changes
if [[ -n $(git status -s) ]]; then
    echo "Error: You have uncommitted changes. Please commit or stash them first."
    exit 1
fi

echo "Switching to gh-pages..."
git checkout gh-pages

echo "Updating application files..."
mkdir -p life-in-the-uk

FILES="index.html questions_base.json service-worker.js manifest.json icon_480.png favicon.ico"

for f in $FILES; do
    # Checkout file from master to current directory (root)
    git checkout master -- $f
    # Move it to the subdirectory
    mv $f life-in-the-uk/
done

# Stage the changes in the subdirectory
git add life-in-the-uk

# Remove the files from the root index (cleaned up from the checkout)
git rm --cached -r $FILES > /dev/null 2>&1

echo "Committing and pushing..."
git commit -m "Deploy update to life-in-the-uk"
git push origin gh-pages

echo "Returning to master..."
git checkout master

echo "Deployment complete! Application available at: https://yiminglin-ai.github.io/life-in-the-uk/"

