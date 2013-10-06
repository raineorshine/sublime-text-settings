#!/bin/bash
cd "~/Library/Application Support/Sublime Text 2"
git add -A
git commit -m "backup `date +%F-%T`"
git push