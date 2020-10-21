#!/usr/bin/python

from youtube_dl import YoutubeDL
from os import system
import utils
system('cls')

if __name__ == '__main__':
    with YoutubeDL(utils.AUDIO_MP3_192) as ydl:
        ydl.download(utils.get_links())
