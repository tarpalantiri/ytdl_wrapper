from . import settings

# Script helpers---------------------------------------------
def get_links_from_file():
    from os import listdir
    
    ls = listdir()
    has_list = settings.LINKS_FILENAME in ls
    if has_list:
        with open(settings.LINKS_FILENAME) as f:
            links = f.readlines()
            cleaned_links = []
            for link in links[:]:
                cleaned_links.append(link.strip())
            return cleaned_links
    else:
        return False #IMPLEMENT LINK CHECKING IN THE FUTURE

def get_links_from_clipboard():
    from pyperclip import paste

    link = paste()
    if 'http' in link:
        return [link]
    else:
        return False #IMPLEMENT LINK CHECKING IN THE FUTURE
#-----------------------------------------------------------


# youtube_dl specific functions-------------------------------------------------
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
#--------------------------------------------------------------------------------   