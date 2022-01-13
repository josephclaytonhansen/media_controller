from flask import Flask, render_template, Response, request, redirect, url_for
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, VK_VOLUME_UP, VK_VOLUME_DOWN, VK_VOLUME_MUTE

app = Flask(__name__)

@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing

@app.route('/play_pause')
@app.route('/next')
@app.route('/back')
@app.route('/up')
@app.route('/down')
@app.route('/mute')

def play_pause():
    print ("Play/Pause")
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return ("nothing")

def next():
    print ("Next")
    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return ("nothing")

def back():
    print ("Back")
    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return ("nothing")

def down():
    print ("Down")
    win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return ("nothing")

def up():
    print ("Up")
    win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return ("nothing")

def mute():
    print ("Mute")
    win32api.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return ("nothing")