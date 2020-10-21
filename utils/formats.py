from .helpers import MyLogger, my_hook

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