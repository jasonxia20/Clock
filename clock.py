import time
settime = eval(input("what hour time is it?"))
settime2 = eval(input("what minute time is it?"))
AMPM = input("AM or PM? (write in all caps)") 
print("setting time...")
time.sleep(3)
if settime2 < 10:
    print("the time is now", settime, ": 0", settime2, AMPM)
    while True:
        time.sleep(60)
        settime2 += 1
        if settime2 % 60 == 0:
            settime += 1
            settime2 = 1
        else:
            settime += 0
        if settime % 12 == 0 and AMPM == "PM":
            settime = 1
            AMPM = "AM"
        else:
            AMPM = "PM"
        if settime % 12 == 0 and AMPM == "AM":
            AMPM = "PM"
        else:
            AMPM = "AM"
        if settime2 < 10:
            print("the time is now", settime, ": 0", settime2, AMPM)
        else:
            print("the time is now", settime, ":", settime2, AMPM)
    
elif settime2 > 59:
    print("please enter a valid time!")
elif settime > 13 or settime < 0:
    print("please enter a valid time!")
else:
    print("the time is now", settime, ":", settime2, AMPM)
    while True:
        time.sleep(60)
        settime2 += 1
        if settime2 % 60 == 0:
            settime += 1
            settime2 = 0
        else:
            settime += 0
        if settime % 12 == 0 and AMPM == "PM":
            settime = 1
            AMPM = "AM"
        else:
            AMPM = "PM"
        if settime % 12 == 0 and AMPM == "AM":
            AMPM = "PM"
        else:
            AMPM = "AM"
        if settime2 < 10:
            print("the time is now", settime, ": 0", settime2, AMPM)
        else:
            print("the time is now", settime, ":", settime2, AMPM)

