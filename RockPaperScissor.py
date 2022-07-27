import random as r
import time
  
# define the countdown func.
def countdown(t):
    mylist = ["scissor","paper ","rock   ",] 
    while t:
        # mins, secs = divmod(t, 60)
        # timer = '{}'.format(secs)
        # print(timer, end="\r")
        print(mylist[t-1], end="\r")

        time.sleep(1)
        t -= 1
   
    x = r.sample(mylist,1)
    print(x[0])
  
# input time in seconds
t = 3
  
# function call
countdown(int(t))

