#!/usr/bin/env python
import os
import subprocess
import time

# reading django db
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'Settopbox_Linux.settings'
django.setup()
from remote_controller.models import StateHolder
def readUserSetting():
    state = StateHolder.objects.all()[0]
    return state

# detect screen
import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk
def detectScreen():
    allmonitors = []

    gdkdsp = Gdk.Display.get_default()
    for i in range(gdkdsp.get_n_monitors()):
        monitor = gdkdsp.get_monitor(i)
        scale = monitor.get_scale_factor()
        geo = monitor.get_geometry()
        allmonitors.append(monitor.get_model())

    return allmonitors

# reading current bandwidth of mediaSharing service
def Check_minidlna(mysudo = '123456'):
    x = subprocess.Popen(['echo ' + mysudo + '|sudo nethogs -c '+"2"+' -t'],shell=True,stdout=subprocess.PIPE)
    x=x.stdout.read()
    x=str(x)
    List_num=[]
    List_x=[]
    num_ref=0
    x=x.split("\\n")
    for i in x:
        x=i.split("\\t")
        

        List_x.append(x)
        num_ref+=1
        if i=='Refreshing:':
            List_num.append(num_ref)

    List_bandwicth_all=[]
    bandwicth_sent=0
    bandwicth_received=0
    
    num_slide=0
    for i in List_num:
        if num_slide==1:
                for p in range(List_num[num_slide],len(List_x)-1):
                    #print(p)
                    List_bandwicth=List_x[p]
                    if 'minidlnad' in  List_bandwicth[0] or '8200' in List_bandwicth[0]:
                        List_bandwicth_all.append(List_bandwicth[1])
                        List_bandwicth_all.append(List_bandwicth[2])

        else:
            for p in range(List_num[num_slide],List_num[num_slide+1]-2):
                    #print(p)
                    List_bandwicth=List_x[p]
                    if 'minidlnad' in  List_bandwicth[0]  or '8200' in List_bandwicth[0] :
                        List_bandwicth_all.append(List_bandwicth[1])
                        List_bandwicth_all.append(List_bandwicth[2])


        num_slide+=1
    
    return List_bandwicth_all


# setup 
previousState = readUserSetting()

# loop
while True: 
    currentState = readUserSetting()
    
    
    if currentState.controlDegree > 0:
        if currentState.controlDegree > 1:
            dlnaActivity = False
            for i in Check_minidlna():
                if float(i) > 0:
                    dlnaActivity = True

            if dlnaActivity:
                currentState.peer2peer = 0
            else:
                currentState.peer2peer = 1

            currentState.save()

        if len(detectScreen()) == 2: # Others screen was on
            currentState.homeEntertain = 1
            currentState.mediaSharing = 0
        else:
            if currentState.homeEntertain == 1:
                currentState.mediaSharing = 0
            else:
                currentState.mediaSharing = 1
        currentState.save()

    if currentState.mediaSharing != previousState.mediaSharing:
        if currentState.mediaSharing == 1: 
            os.system("minidlnad -f /home/kong/.minidlna/minidlna.conf -P /home/kong/.minidlna/minidlna.pid")
        else:
            os.system("xargs kill </home/kong/.minidlna/minidlna.pid")
    
    if currentState.homeEntertain != previousState.homeEntertain:
        if currentState.homeEntertain == 1:
            os.system('kodi &')
        else:
            os.system('pkill kodi')

    if currentState.peer2peer != previousState.peer2peer:
        if currentState.peer2peer == 1:
            os.system('deluge &')
        else:
            os.system('pkill deluge')

    previousState = currentState
    time.sleep(2)