#!/bin/bash

# Define an alias in your shell rc file for easy backup from anywhere
# alias backupsublime="~/Library/Application\ Support/Sublime\ Text/backup.sh"

pushd ~/Library/Application\ Support/Sublime\ Text
git add -A
git commit -m "backup `date +%F-%T`"
git push
popd