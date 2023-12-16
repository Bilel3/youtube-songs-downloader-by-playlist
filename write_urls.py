import os
import urllib.request
import json
from bs4 import BeautifulSoup

def get_youtube_url(keyword):
    api_key = "AIzaSyAE0mlrKZ-R5-9AVym8Mbi9t9zKnOayQ54"  # Replace with your YouTube Data API key

    # Encode the keyword for the YouTube search URL
    encoded_keyword = urllib.parse.quote(keyword, safe='')

    # Construct the YouTube search URL
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={encoded_keyword}&type=video&key={api_key}"

    with urllib.request.urlopen(search_url) as response:
        data = json.load(response)

        if "items" in data and data["items"]:
            video_id = data["items"][0]["id"]["videoId"]
            return f'https://www.youtube.com/watch?v={video_id}'
        else:
            print(f"No video found for: {keyword}")
            return None

def main():
    input_file_path = "music-list.txt"  # Change this to your input file path
    output_file_path = "urls.txt"  # Change this to your output file path

    with open(input_file_path, 'r') as input_file:
        keywords = input_file.readlines()

    with open(output_file_path, 'w') as output_file:
        for keyword in keywords:
            keyword = keyword.strip()
            youtube_url = get_youtube_url(keyword)

            if youtube_url:
                output_file.write(f"{keyword}: {youtube_url}\n")

    print(f"URLs written to {output_file_path}")

if __name__ == '__main__':
    main()
