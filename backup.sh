#!/bin/bash
pushd ~/Library/Application\ Support/Sublime\ Text\ 3/
git add -A
git commit -m "backup `date +%F-%T`"
git push
popd