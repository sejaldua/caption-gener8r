

for file in profiles/*.json
do
    mv "$file" "${file/ /_}"
done

# rm profiles/*
