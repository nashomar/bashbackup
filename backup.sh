#!/bin/bash

source=$1
destination=$2

if [[ $target == *"@"* ]]; 
    then
      ssh "$target" "mkdir $(date +%Y-%m-%d)"
        rsync -avEPhz "$source" "$target:$(date +%Y-%m-%d)/"
else
    mkdir "$target/$(date +%Y-%m-%d)"
      rsync -avEPhz "$source" "$target/$(date +%Y-%m-%d)/"
fi