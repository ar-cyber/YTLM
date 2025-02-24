# YTLM

YouTube Live Music  (YTLM) is a stupid little bot I coded (with a little help from AI) that allows viewers of a live stream to use commands to queue music

# Contents:

[Commands](#COMMANDS "Commands")
\-	[!queue](-!queue "#!queue")
[Setup](#SETUP)
[Notes](#NOTES)

## COMMANDS

### !queue

The command to queue a song is "!queue \<VIDEO\_ID>" where \<VIDEO\_ID> is the unique string of characters used to identify a video (everything after the "v=")&#x20;

:::caution
THIS COMMAND ONLY WORKS WITH IDs OF VIDEOS THAT ARE ON YOUTUBE MUSIC, REGULAR VIDEOS WILL NOT DOWNLOAD
:::

## SETUP

1. Clone/Download and extract the Repo to any folder on your computer
2. Install [Python](https://www.python.org/downloads/). During installation, please make sure the boxes at the bottom labelled "add Python.exe to PATH" and "Use admin privileges when installing" are ticked
3. install dependencies (found in Src/requirements.txt) or run the file "Src/PipInstallBat.bat" on Windows to install dependencies
4. Install [VLC](https://www.videolan.org/vlc/) x86
5. Download the correct [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip) version, extract it and navigate to the bin folder
6. Move everything from the bin folder to src/ffmpeg and then delete the placeholder file "DELETEME"
7. Locate the path of the VLC media player, generally found in "C:\Program Files\VideoLAN\VLC" or "C:\Program Files (x86)\VideoLAN\VLC"
8. Open the file "config.json" in your text editor of choice, I recommend [VsCode](https://code.visualstudio.com/download) or [Notepad++](https://notepad-plus-plus.org/downloads/v8.6.7/)
9. Change "YOUR\_LIVESTREAM\_ID" to the ID of your live stream (Ie. the characters at the end of the URL, after the "/live/")
10. Change the value for "RATE\_LIMIT\_SECONDS". This defaults to 600 and is how long users have to wait before they can request another song (in seconds)
11. Replace "PATH\_TO\_VLC\_HERE" with the path to your VLC&#x20;
12. Run main.py, VLC will open.

:::danger
***USE DOUBLE BACKSLASHES INSTEAD OF SINGLE, "C:\Program Files\VideoLAN\VLC" MUST BECOME "C:\Program Files\VideoLAN\VLC\vlc.exe"***
:::

:::tip
Please turn off loop mode in VLC otherwise if the song queue runs out you will have to listen to the whole playlist again before you get to the new ones
:::

## NOTES

-This program can be run on any Windows PC with no API key or cookie required, if used, please credit me in the description or somewhere in the video
-This program Has not been tested on any other OS and it is unknown if it works

## STAR HISTORY

[![Star History Chart](https://api.star-history.com/svg?repos=NIDNHU/YTLM\&type=Date)](https://star-history.com/#NIDNHU/YTLM\&Date)

PFP image by Craiyon
