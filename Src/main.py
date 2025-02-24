import time
import pytchat
import re
import json
from collections import defaultdict
import webbrowser

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

YOUTUBE_VIDEO_ID = config.get("YOUTUBE_VIDEO_ID", "YOUR_LIVESTREAM_ID")
RATE_LIMIT_SECONDS = config.get("RATE_LIMIT_SECONDS", 600)

user_last_command = defaultdict(lambda: 0)

# Video queue
video_queue = []

def play_next_video():
    """Plays the next video in the queue."""
    if video_queue:
        next_video = video_queue.pop(0)
        print(f"Now playing: {next_video}")
        webbrowser.open(next_video)
        play_next_video()  # Recursively play next video
    else:
        print("Queue is empty. Waiting for new videos...")

def is_valid_youtube_url(url):
    """Check if a URL is a valid YouTube video link."""
    pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+"
    return re.match(pattern, url)

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
        
        youtube_url = parts[1]
        
        if not is_valid_youtube_url(youtube_url):
            print(f"{username} tried to queue an invalid YouTube link.")
            return
        
        # Enforce rate limit
        if current_time - user_last_command[username] < RATE_LIMIT_SECONDS:
            print(f"{username} is sending commands too fast! Ignored.")
            return
        
        # Add to queue and update rate limit
        video_queue.append(youtube_url)
        user_last_command[username] = current_time
        print(f"{username} added to queue: {youtube_url}")
        
        # If nothing is playing, start playback
        if len(video_queue) == 1:
            play_next_video()

# Start listening to YouTube chat
def start_chat_listener():
    print("Listening to YouTube Live Chat...")
    chat = pytchat.create(video_id=YOUTUBE_VIDEO_ID)
    while chat.is_alive():
        for message in chat.get().sync_items():
            on_chat_message(message)
        time.sleep(1)

if __name__ == "__main__":
    start_chat_listener()
