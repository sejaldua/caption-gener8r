import json
import os
import numpy as np
import pandas as pd

identifier = []
photos = []
captions = []
valid_collections = 0
photo_dump = 0
num_valid = 0
num_dump = 0
no_image = 0
no_caption = 0
has_quotes = 0
for fn in os.listdir("profiles_sejal/"):
    if fn.endswith(".json"):
        f = open("profiles_sejal/" + fn)
        data = json.load(f)
        try:
            posts = data["posts"]
        except:
            print(fn)
            exit
        for p in posts:
            if len(p["imgs"]) > 1:
                if len(p["imgs"]) > 2:
                    photo_dump += 1
                    num_dump += len(p["imgs"])
                else:
                    valid_collections += 1
                    num_valid += len(p["imgs"])
            elif len(p["imgs"]) == 0:
                no_image += 1
            elif p["caption"] == "":
                no_caption += 1
            else:
                identifier.append(data["username"])
                photos.append(p["imgs"][0])
                if '"' in p["caption"]:
                    has_quotes += 1
                captions.append(p["caption"].replace('"', '\''))
        f.close()

total = len(captions) + photo_dump + 2*valid_collections + no_image + no_caption
print("throwing out:", photo_dump + no_image + no_caption, round((photo_dump + + no_image + no_caption) * 100 / total, 2))
print("\t no caption", no_caption, round((no_caption / total) * 100, 2))
print("\t no image", no_image, round((no_image / total) * 100, 2))
print("usable:", len(captions) + 2*valid_collections, round((len(captions)+2*valid_collections)*100/total, 2))
print("\tvalid collections:", valid_collections * 2, round(2*valid_collections* 100 / total, 2))
print("\tvalid single photos:", len(captions), round(len(captions)*100/total, 2))

with open('data_sejal.csv', 'w') as f:
    f.write("username,photo,caption\n")
    for i in range(len(photos)):
        f.write("%s,%s,\"%s\"\n" % (identifier[i],photos[i], captions[i]))
f.close()

try:
    csv = pd.read_csv("data_sejal.csv", header=0)
    csv.drop_duplicates(keep="first",inplace=True)
    csv.to_csv("data_sejal.csv", index=False)
except:
    print('pandas stuff did not work')
