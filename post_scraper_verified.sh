#!/bin/bash
input="verified.txt"
args=""
space=" "
while IFS= read -r line
do
  args="${args} "
  args="$args$line"
done < "$input"
python crawl_profile.py $args
