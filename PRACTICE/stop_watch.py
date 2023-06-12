#---------------STOP WATCH--------
import time

time_limit = int(input("Enter the stopwatch time.: "))

# hours = int(time_limit/3600)
# minutes = int(time_limit/60) % 60
# seconds = (time_limit) % 60

# print(hours,minutes,seconds)


for x in range(time_limit,0,-1):
    seconds = (x) % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    time.sleep(1)   # it'll delay o/p by given sec
    print(f"{hours:02}:{minutes:02}:{seconds:02}")


    # print(minutes,"minutes left",":",seconds,"seconds left")

