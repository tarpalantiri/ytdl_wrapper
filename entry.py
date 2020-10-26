#!/usr/bin/python

from youtube_dl import YoutubeDL
from os import system
from utils import settings, helpers
system('cls')

if __name__ == '__main__':
    system('cls')
    print(settings.GREET_MESSAGE)
    option = input('[ 1/2 ] -> ')
    with YoutubeDL(settings.AUDIO_MP3_192) as ydl:
        if option == 1:
            links = helpers.get_links_from_file()
        else:
            links = helpers.get_links_from_clipboard()
        ydl.download(links)
