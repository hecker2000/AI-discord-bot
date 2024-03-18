# AI-discord-bot
a simple Python script for making an AI chatbot in discord

# How to install
_This is only meant for Windows_

you will need 3 dependencies for the script to work:

1. discord.py (https://pypi.org/project/discord.py/)
2. ffmpeg (https://www.ffmpeg.org/download.html)
3. gpt4all (https://docs.gpt4all.io/gpt4all_python.html)

then you will need to open the script to insert file locations. after line 35, you shouldn't need to edit anything else 
(other than changing a discord ID to not be mine lol)

# default commands and ignoring text
by using the prefix ":" the bot will ignore you, to get the AI to run commands simply type some of the following text into a channel the bot is in.
1. : clear (clears the bot's current memory)
2. : vc {optional: integer} (makes the bot join the VC you are currently in and plays a random sound that you can specify)
3. : leave (leaves the server the command was sent in)

# TODO
* add linux support.
* build a wiki
* add more commands
* fix chat4AI bug
