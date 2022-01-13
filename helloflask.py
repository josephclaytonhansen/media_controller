from flask import Flask, render_template, Response, request, redirect, url_for
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, VK_VOLUME_UP, VK_VOLUME_DOWN, VK_VOLUME_MUTE

app = Flask(__name__)

@app.route('/json', methods=['GET', 'POST'])
def json():
    g = request.full_path
    print(g)
    cmds = ["play", "next", "back", "up", "down", "mute"]
    for c in cmds:
        if c in g:
            print(c)
            execute(c)
    else:
        pass # unknown
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('json.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
def execute(p):
    d = {"play":VK_MEDIA_PLAY_PAUSE,
         "next":VK_MEDIA_NEXT_TRACK,
         "back":VK_MEDIA_PREV_TRACK,
         "up":VK_VOLUME_UP,
         "down":VK_VOLUME_DOWN,
         "mute":VK_VOLUME_MUTE}
    print(d[p])
    win32api.keybd_event(d[p], 0, KEYEVENTF_EXTENDEDKEY, 0)
    
    