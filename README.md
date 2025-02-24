# YTLM
YouTube Live Music  (YTLM) is a bot i coded (with the help of AI) that allows viewers of a livestream to use commands to queue music

# SETUP
1- Clone/Download and extract the Repo to any folder on your computer

2- Run the file "PipInstall.bat"

3- Install [VLC](https://www.videolan.org/vlc/) x86

4- Download the correct [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip) version, extract it and navigate to the bin folder

5- Move everything from the bin folder to src/ffmpeg and then delete the placeholder file "DELETEME"

4- Locate the path of VLC media player, generally found in "C:\Program Files\VideoLAN\VLC\" or "C:\Program Files (x86)\VideoLAN\VLC\"

5- Open the file "config.json" in your text editor of choice, I reccomend [VsCode](https://code.visualstudio.com/download) or [Notepad++](https://notepad-plus-plus.org/downloads/v8.6.7/)

6- Change "YOUR_LIVESTREAM_ID" to the ID of your livestream (Ie. the characters at the end of the URL, after the "/live/")

7- Change the value for "RATE_LIMIT_SECONDS" this defaults to 600 and is how long users have to wait before they can request another song (in seconds)

8- Replace "PATH_TO_VLC_HERE" with the path to your VLC ***USE DOUBLE BACKSLASHES INSTEAD OF SINGLE, "C:\Program Files\VideoLAN\VLC\" MUST BECOME "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"***

9- ***TURN OFF LOOP IN VLC!!!***

10- Run main.py, VLC will open, please turn off loop otherwise if you run out of songs you will have to listen to the whole playlist again before you get to the new ones

# NOTES
This program can be run on ANY WINDOWS PC, no key or api is required, if used, please credit me in the description or somewhere in the video


