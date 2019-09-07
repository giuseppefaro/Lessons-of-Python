import time

def QuickWash ():
    print("Quick Wash program is now starting\n")
    t=6
    time.sleep(0.5)
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining Time to complete the washing task:', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("Wash completed                                            ",  end='\r')
    print("")
    time.sleep(1)    
    Rinse()
       


def Normal ():
    print("Normal program is now starting\n")
    time.sleep(0.5)
    t=10
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining Time to complete the washing task:', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("Wash completed                                                  ",  end='\r')
    print("")
    time.sleep(1)
    Rinse()
    

def Cotton ():
    print("Cotton program is now starting\n")
    time.sleep(0.5)
    t=10
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining Time to complete the washing task:', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("Wash completed                                        ",  end='\r')
    print("")
    time.sleep(1)
    Rinse()
    

def Rinse ():
    print("Rinse program is now starting\n")
    time.sleep(0.5)
    t=5
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining Time:', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("Rinse completed             ",  end='\r')
    time.sleep(1)
    print("")
    Spin()

def Spin ():
    print("Spin program is now starting\n")
    time.sleep(0.5)
    t=3
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining Time to complete the washing task:', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    time.sleep(0.5)
    print ("The washing machine complete all the programs, please remove your clothes          ", end='\r')
    print("")
