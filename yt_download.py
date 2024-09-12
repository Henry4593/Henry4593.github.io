#!/usr/bin/python3
from pytube import YouTube
import sys
url = sys.argv[1]

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download()
        print('Video downloaded successfully!')
    except Exception as e:
        print(f'Error downloading video: {str(e)}')

# Example usage
if __name__ == "__main__":
    download_video(url)
