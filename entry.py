#!/usr/bin/python

from youtube_dl import YoutubeDL
from os import system
from utils import settings, helpers
system('cls')

if __name__ == '__main__':
    with YoutubeDL(settings.AUDIO_MP3_192) as ydl:
        links = helpers.get_links()
        if links:
            ydl.download(links)
        else:
            print('Invalid or empty list file detected...')
