#!/usr/bin/python

from youtube_dl import YoutubeDL
from os import system
from utils import formats, helpers
system('cls')

if __name__ == '__main__':
    with YoutubeDL(formats.AUDIO_MP3_192) as ydl:
        ydl.download(helpers.get_links())
