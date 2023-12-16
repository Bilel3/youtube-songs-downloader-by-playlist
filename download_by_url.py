import argparse
from pytube import YouTube
VIDEO_DOWNLOAD_DIR = "/app/downloads"
AUDIO_DOWNLOAD_DIR = "/app/downloads"


def YoutubeAudioDownload(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(AUDIO_DOWNLOAD_DIR)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required = True, help = "Youtube video URL")
    ap.add_argument("-a", "--audio", required = False, help = "Audio only", action = argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())

    if args["audio"]:
        YoutubeAudioDownload(args["video"])
    else:
        YoutubeVideoDownload(args["video"])