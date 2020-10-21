# filetypes.py

def get_links():
    vid_links = []
    list_file = 'list.txt'
    from os import listdir
    
    if list_file in listdir():
        with open(list_file) as f:
            vid_links = f.readlines()
            return vid_links
    else:
        vid_links = input("Paste the video link: ")
        return vid_links

class MyLogger(object):
    def debug(self, msg): pass

    def warning(self, msg): pass

    def error(self, msg): pass



def my_hook(d):
    if d['status'] == 'finished':
        print('Download Done. Converting...')

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