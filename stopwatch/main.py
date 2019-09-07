import time
import sys
from playsound import playsound
# run only on python3
if (sys.version_info < (3, 0)):
    #Python 2 code in this block
    print('This script is not compatible with Python2, please run it on Python3')
    exit
else:
    #Python 3 code in this block
    print('StopWatch with alarm')
    print ()
    print('How many minutes')
    m = int(input())
    print ()
    print('How many seconds')
    s = int(input())
    print ()

## convert time in seconds
minconv = m*60
t=minconv+s

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining Time:', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Done                  ')
    playsound('alarm.mp3')

countdown(t)

