from mutagen.easyid3 import EasyID3
import os
import re
import csv

# Strip video id
fileList = os.listdir();
for file in fileList:
    if not file.endswith('.mp3'):
        pass
    else:
        os.rename(file, re.sub(r' *\[.*\] *', '', file))

# Add tags from input.csv file
# Expect 3 columns: tracknumber, title, artist
# Expect no header
with open('input.csv') as input:
    inputReader = csv.reader(input)
    for row in inputReader:
        audio = EasyID3(row[1] + '.mp3')
        audio["tracknumber"] = row[0]
        audio["title"] = row[1]
        audio["artist"] = row[2]
        audio.save()

