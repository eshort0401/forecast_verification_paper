#!/bin/bash
# Store username details in cache for one hour
git config --global credential.helper 'cache --timeout=3600'
git add --all
git commit -m "$1"
git push origin master
