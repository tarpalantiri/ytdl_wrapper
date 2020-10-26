from .helpers import MyLogger, my_hook

LINKS_FILENAME = 'list.txt'

GREET_MESSAGE = """
#######################################################################
#  __     ______  _    _ _______ _    _ ____  ______   _____  _       #
#  \ \   / / __ \| |  | |__   __| |  | |  _ \|  ____| |  __ \| |      #
#   \ \_/ / |  | | |  | |  | |  | |  | | |_) | |__    | |  | | |      #
#    \   /| |  | | |  | |  | |  | |  | |  _ <|  __|   | |  | | |      #
#     | | | |__| | |__| |  | |  | |__| | |_) | |____  | |__| | |____  #
#     |_|  \____/ \____/   |_|   \____/|____/|______| |_____/|______| #
#                                                                     #
#######################################################################

Script Author: Tehseen Sajjad
Written in: Python 3.8
Uses the youtube_dl library
Check https://github.com/tarpalantiri/ytdl_wrapper for usage and source :)

1. GET LINKS FROM LOCAL FILE
2. GET LINKS FROM CLIPBOARD
"""

AUDIO_MP3_192 = {
    'format' : 'bestaudio/best',
    'logger' : MyLogger(),
    'progress_hooks' : [my_hook],
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192',
    }]
}