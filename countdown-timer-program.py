import time
myTime=int(input("Enter the time in seconds: "))

for x in range (myTime, 0, -1):
    seconds =int(x%60) #to make sure that the seconds dont go past 60. 
    minutes =int( (x/60)%60)
    hours =int((x/3600)%60)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME IS UP!!!!")