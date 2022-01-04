import os
import time

def Update():
    os.system('git add -A')
    os.system('git commit -m' + '"' + time.strftime("%d/%m/%Y" + ' ' + "%H:%M:%S") + '"')
    os.system('git push')