import os
import subprocess
#os.system('firefox')
#os.system('pkill transmission')
#os.system('pgrep oneshort')
def Kill_program(Name):
    try:
        os.system('pkill '+Name)
        print(888)
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
        
'''print(openfile())
openfile()
Kill_program('transmission')'''
Dirt_value_all={}
import time

def Check_total_bandwidth():

    x = subprocess.Popen(['sudo nethogs -c '+"10"+' -t'],shell=True,stdout=subprocess.PIPE)
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
        if num_slide==9:
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
        #Dirt_value_all[time_count]=List_bandwicth_all
    return List_bandwicth_all[-2],List_bandwicth_all[-1]
def Check_minidlna():
    x = subprocess.Popen(['sudo nethogs -c '+"10"+' -t'],shell=True,stdout=subprocess.PIPE)
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
        if num_slide==9:
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
    
    return List_bandwicth_all    #Dirt_value_all[time_count]=List_bandwicth_all
    #return List_bandwicth_all[-2],List_bandwicth_all[-1]

def return_loop(Program):
    num=0
    #Program_close=Kill_program(Program)
    while str(subprocess.Popen(['pgrep '+Program],shell=True,stdout=subprocess.PIPE).stdout.read())!="b''":
        num+=1
        x=Check_total_bandwidth()
        Dirt_value_all['Set'+str(num)]=[x]
        print(Dirt_value_all)
    return Dirt_value_all
def return_loop_minidlna():
    count=True
    while str(subprocess.Popen(['pgrep minidlna'],shell=True,stdout=subprocess.PIPE).stdout.read())!="b''":
        x=Check_minidlna()
        if x!=[]:
            x=[x[-2],x[-1]]
        print(x)
    
        
    

#Check_total_bandwidth()
#return_loop_all('transmission')
#print(Dirt_value_all)

#x=os.system('pkill transmission')
#x=subprocess.check_output('pgrep transmission',shell=True)
#x=Kill_program('transmission')
#print(x)
# x = subprocess.Popen(['apropos transmission'],shell=True,stdout=subprocess.PIPE)
# x=x.stdout.read()
# x=str(x)
# x=x.split('\\n')
#print(x)
# print(Check_minidlna())
return_loop_minidlna()