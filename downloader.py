import os
import urllib.request
import json
from os import system
import sys

def titleCase(s):
    l = s.split()
    str = l[0][0].upper() + l[0][1:]

    for word in l[1:]:
        if word not in ['in', 'the', 'for', 'of', 'a', 'at', 'an', 'is', 'and']:
            str += ' ' + word[0].upper() + word[1:]
        else:
            str += ' ' + word

    return str

pathToSave = "/app/downloads"  # Change this to your desired path

def getVideoId(song):
    api_key = "AIzaSyAE0mlrKZ-R5-9AVym8Mbi9t9zKnOayQ54"  # Replace with your YouTube Data API key
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={song}&type=video&key={api_key}"

    with urllib.request.urlopen(search_url) as response:
        data = json.load(response)

        if "items" in data and data["items"]:
            video_id = data["items"][0]["id"]["videoId"]
            return video_id
        else:
            print(f"No video found for: {song}")
            return None

def doStuff(song):
    print("Downloading " + titleCase(song))
    video_id = getVideoId(song)

    if video_id:
        # Use ytsearch1 extractor explicitly
        link = f'https://www.youtube.com/watch?v={video_id}'
        system(f"youtube-dl --extractor ytsearch1 -x -q -o '{pathToSave + titleCase(song)}.%(ext)s' '{link}'")
        print("Downloaded " + titleCase(song) + "\n")

def main():
    print('-------------------------------------------------------------')
    if len(sys.argv) == 3 and (sys.argv[1] == '-i' or sys.argv[1] == '-I'):
        for song in open(sys.argv[2]).readlines():
            doStuff(song.strip())
    else:
        for song in sys.argv[1:]:
            doStuff(song)

if __name__ == '__main__':
    main()
