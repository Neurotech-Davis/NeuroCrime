

# pip install yt-dlp
import yt_dlp
import os

# Directory to save the video, feel free to rename
SAVE_PATH = "./vids"
os.makedirs(SAVE_PATH, exist_ok=True)

# Video URL, change everytime you want to download something
video_url = "https://www.youtube.com/watch?v=tZoHb2ZdlVw" # !!!!

# Use an extension (get cookies.txt Locally is what I used) while on Youtube page, and rename cookies.txt
use_cookies_file = True
cookies_file_path = "./cookies.txt" 

ydl_opts = {
    "outtmpl": f"{SAVE_PATH}/%(title)s.%(ext)s",
    "format": "bestvideo+bestaudio/best",
    "noplaylist": True,  
    "postprocessors": [],
    "verbose": True,
}

if use_cookies_file:
    ydl_opts["cookiefile"] = cookies_file_path
else:
    ydl_opts["cookiesfrombrowser"] = ("chrome",)

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        video_streams = [stream for stream in info['formats'] if stream.get('vcodec') != 'none']
        best_video = max(video_streams, key=lambda x: x['height'])  # Pick highest resolution

        print(f"Downloading best video-only stream: {best_video['format_note']} at {best_video['height']}p")
        ydl.download([f"{video_url}"])
    print("Video downloaded successfully!")
except Exception as e:
    print(f"Error during download: {e}")
