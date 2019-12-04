#!/bin/bash
input="followers/erikaaanakagawa_followers.txt"
args=""
space=" "
while IFS= read -r line
do
  args="${args} "
  args="$args$line"
  echo $args
done < "$input"
python crawl_profile.py $args
