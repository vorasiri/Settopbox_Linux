import glob
from pathlib import Path
import os
def openfile():
    for i in glob.glob('/home/*/*/'):
        i=Path(i)
        for file in i.glob('*.torrent'):
            Lastfile=file
    Lastfile=str(Lastfile)
    return (Lastfile)
    #return os.system('xdg-open '+Lastfile)
        
print(openfile())