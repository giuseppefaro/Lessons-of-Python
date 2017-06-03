###                                                                                         ###
#   this exercise is to demonstrate easily how import the value into  different functions      #
###                                                                                         ###

import time

# this function do a simple multiplication from the Input Variable and the constant "B"
def first(a):
    b = 3
    return (a*b)
#time.sleep(1)

# this function do a simple multiplication from the "return value" from the "First Function"
def second(first):
    print ('This is the value imported from the "Return of the Function first" in the Second Function', first)
    print ('')
    return first*2

print('###                                                                                         ###\n'
      '#   this exercise is to demonstrate easily how import the value into different functions      #\n'
      '###                                                                                         ###\n')

a1 = input('Insert a Number : ')
# The variable "A1" need to be converted or python think is a "str" and not "int"
a = int(a1)
time.sleep(1)
print ( 'The result from the first function is =',first(a))
print ('\n')
time.sleep(1)
print ('This one is the Output from the Return of the Second Function',second(first(a)))

time.sleep(5)

input('\nPress a key to exit ;)')

#thank you !!