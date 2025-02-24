import time
import pytchat
import re
import json
import subprocess
from collections import defaultdict
import yt_dlp

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

YOUTUBE_VIDEO_ID = config.get("YOUTUBE_VIDEO_ID", "YOUR_LIVESTREAM_ID")  # For chat connection
RATE_LIMIT_SECONDS = config.get("RATE_LIMIT_SECONDS", 600)
VLC_PATH = config.get("VLC_PATH", "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")  # Default path if not set

user_last_command = defaultdict(lambda: 0)

# Video queue
video_queue = []

def play_next_video():
    """Plays the next video in the queue using VLC."""
    while video_queue:
        next_video_id = video_queue.pop(0)
        video_url = f"https://music.youtube.com/watch?v={next_video_id}"  # Construct the YouTube Music URL
        
        print(f"Now playing: {video_url}")
        
        # Use yt-dlp to get the video URL and play it with VLC
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(video_url, download=False)  # Extract info without downloading
                audio_url = info['url']
                
                # Launch VLC with the audio URL
                subprocess.Popen([VLC_PATH, audio_url])
            except Exception as e:
                print(f"Error playing video: {e}")

        time.sleep(2)  # Add a short delay to avoid rapid playback

def is_valid_youtube_music_video_id(video_id):
    """Check if a video ID is a valid YouTube Music video ID."""
    return re.match(r"^[\w-]{11}$", video_id) is not None  # YouTube video IDs are typically 11 characters long

def on_chat_message(chat):
    """Handles incoming chat messages."""
    global user_last_command
    username = chat.author.name
    message = chat.message
    current_time = time.time()
    
    # Check if the message starts with !queue
    if message.startswith("!queue"):
        parts = message.split()
        if len(parts) < 2:
            return  # Ignore invalid command format
        
        youtube_video_id = parts[1]
        
        if not is_valid_youtube_music_video_id(youtube_video_id):
            print(f"{username} tried to queue an invalid YouTube Music video ID.")
            return
        
        # Enforce rate limit
        if current_time - user_last_command[username] < RATE_LIMIT_SECONDS:
            print(f"{username} is sending commands too fast! Ignored.")
            return
        
        # Add to queue and update rate limit
        video_queue.append(youtube_video_id)
        user_last_command[username] = current_time
        print(f"{username} added to queue: {youtube_video_id}")
        
        # If nothing is playing, start playback
        if len(video_queue) == 1:
            play_next_video()

# Start listening to YouTube chat
def start_chat_listener():
    print("Listening to YouTube Live Chat...")
    chat = pytchat.create(video_id=YOUTUBE_VIDEO_ID)
    
    if not chat.is_alive():
        print("Failed to connect to the chat. Please check the video ID.")
        return
    
    print("Connected to the chat. Listening for messages...")
    
    while chat.is_alive():
        messages = chat.get().sync_items()  # Use sync_items() to get an iterable of messages
        for message in messages:  # Iterate over the list of messages
            if message.author.name and message.message:
                print(f"{message.author.name}: {message.message}")  # Log all messages
                on_chat_message(message)  # Handle chat messages for song queuing
        time.sleep(0.5)  # Reduce sleep time for faster processing

if __name__ == "__main__":
    start_chat_listener()
