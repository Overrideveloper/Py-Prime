#Owner: Overrideveloper
#Description: GCD Program 

from datetime import datetime
import os
import psutil

startTime = datetime.now()

lowerbound = int(input("Enter lower bound: /n"))

upperbound = int(input("Enter upperbound: /n"))

for num in range(lowerbound,upperbound):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            break
        else:
            print(num)
        
#My phone fell and broke while writing this. :( 

process = psutil.Process(os.getpid())
print ("The execution time is ",(datetime.now()- startTime))

print("Memory consumption in Kilobytes is: ")
print(process.memory_info().rss / 1024)
