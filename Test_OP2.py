import os
import subprocess
#os.system('firefox')
#os.system('pkill transmission')
#os.system('pgrep oneshort')
def Kill_program(Name):
    try:
        os.system('pkill '+Name)
    except (Exception) as e:
        print(e)


import glob
from pathlib import Path
import os
def openfile():
    global Lastfile
    for i in glob.glob('/home/*/*/'):
        i=Path(i)
        for file in i.glob('*.torrent'):
            Lastfile=file
    Lastfile=str(Lastfile)
    #return (Lastfile)
    return os.system('xdg-open '+Lastfile)
        
print(openfile())
openfile()
Kill_program('transmission')

def Check_total_bandwidth(Loop):
    x = subprocess.Popen(['sudo nethogs -c '+Loop+' -t'],shell=True,stdout=subprocess.PIPE)
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
        if num_slide==int(Loop)-1:
                for p in range(List_num[num_slide],len(List_x)-1):
                    #print(p)
                    List_bandwicth=List_x[p]
                    #print(List_bandwicth)
                    bandwicth_sent=bandwicth_sent+float(List_bandwicth[1])
                    bandwicth_received=bandwicth_received+float(List_bandwicth[2])
                    #print(bandwicth_sent)
        else:
            for p in range(List_num[num_slide],List_num[num_slide+1]-2):
                    #print(p)
                    List_bandwicth=List_x[p]
                    #print(List_bandwicth)
                    bandwicth_sent=bandwicth_sent+float(List_bandwicth[1])
                    bandwicth_received=bandwicth_received+float(List_bandwicth[2])
                    #print(bandwicth_sent)
        List_bandwicth_all.append(bandwicth_sent)
        List_bandwicth_all.append(bandwicth_received)
        num_slide+=1

    return (List_bandwicth_all)
print(Check_total_bandwidth('5'))
