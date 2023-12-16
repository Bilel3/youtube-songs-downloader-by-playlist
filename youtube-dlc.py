import subprocess

def download_mp3_from_file(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                download_mp3(url)

def download_mp3(url):
    try:
        subprocess.run(['youtube-dlc', '--extract-audio', '--audio-format', 'mp3', '--audio-quality', '0', url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    input_file_path = "keywords.txt"  # Replace with the path to your file containing URLs

    download_mp3_from_file(input_file_path)
