from pyperclip import paste

def get_links():
    """
    Function to get the link(s) for YoutubeDL.download
    first it checks for a file list.txt and gets the links from it
    if the file doesnt exist or the file doesnt have any links,
    it gets the link from your clipboard
    """
    from os import listdir

    list_file = 'list.txt'
    links = []
    if list_file in listdir():
        filehandle = open(list_file)
        links = filehandle.readlines()
        filehandle.close()
        if links:
            return links
        else:
            return False
    else:
        clipboard_link = paste()
        print(
            f"Using {clipboard_link} from clipboard..."
        )
        links.append(clipboard_link)
        return links

class MyLogger(object):
    def debug(self, msg): pass

    def warning(self, msg): pass

    def error(self, msg): pass



def my_hook(d):
    if d['status'] == 'finished':
        print('Download Done. Converting...')
    if d['status'] == 'downloading':
        print(
            f"Downloading {d['filename']} {d['_percent_str']} {d['_eta_str']}"
        )
        