import sys
from program import *
from playsound import playsound

print('This script is not compatible with Python2, please run it on Python3')


print ('Press a number to start the selected program')
print ()
selection = ['0. QuickWash', '1. Normal','2. Cotton','3. Rinse','4. Spin'] 
print(*selection, sep = "\n") 
print ()
p = int(input())
# add in range of a.lengt
s = selection[p]
s1=(s[3:])
print(s1)

### this line allow to call a function from a sting
locals()[s1]()


playsound("tone.mp3")
exit