#!/usr/bin/env python3

import sys,os
from gi.repository import Gtk, Gdk
import speachlib 
import time

minc=0
back=''
last=0


crdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(crdir)


sh = {"am":"espeak -v hy  -f '/tmp/ttsdata'",
      "en":"espeak -v en  -f '/tmp/ttsdata'",
      "ru":"cat /tmp/ttsdata | RHVoice-client -v 1 -s anna+clb | aplay",
}

def callBack(*args):
    global back
    global last
    speachlib.killspeach()
    text = clip.wait_for_text()
    lng = speachlib.getLang(text)
    #if lng == 'ru':
    #    text = speachlib.russianfix(text)
    f = open('/tmp/ttsdata',"w")
    f.write(text)
    f.close()
    if text.find('http') == 0 or text.find('www') == 0:
        return 0
    if back == text and (time.time()-last>75):
        return 0
    if time.time()-last<1.0:
    	return 0    
    os.system(sh[lng]+' &')
    back=text
    last=time.time()
def oops(*arg):
    speachlib.killspeach()
    exit()

def minw(*arg):
    global minc
    if minc==0:
        time.sleep(0.2)
        minc=1
        os.system('xdotool windowminimize $(xdotool getactivewindow)')

def killsh(*arg):
	speachlib.killspeach()

window = Gtk.Window()
button = Gtk.Button("Stop TTS")
button.connect("clicked", killsh , None)

button.show()

window.add(button)


clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clip.connect('owner-change',callBack)
window.connect("destroy",oops)
window.connect("focus_in_event",minw)
window.reshow_with_initial_size()
window.resize(120,80)
Gtk.main()
