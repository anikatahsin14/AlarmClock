from datetime import datetime           #module to import sound
from playsound import playsound         #module to import current time
import time
alarmTime = input("Set Time: ")   
def validate_time(alarmTime):           #function for checking the time input by the user
    if len(alarmTime) != 11:
        return "Invalid time! Please try again..."
    else:     #using slicing operator to store the particular unit of time into certain variables
        if int(alarmTime[0:2]) > 12:
            return "Invalid HOUR! Please try again..."
        elif int(alarmTime[3:5]) > 59:
            return "Invalid MINUTE! Please try again..."
        elif int(alarmTime[6:8]) > 59:
            return "Invalid SECOND! Please try again..."
        else:
            return "ALARM SAVED!"
    while True:
        alarmTime = input("Set Time: ")
        validate = validate_time(alarm_time.lower())
        if validate != "ok":
           print(validate)
        else:
           print(f"Setting alarm for {alarmTime}...")
           break        
alarm_hour = alarmTime[0:2]
alarm_min = alarmTime[3:5]
alarm_sec = alarmTime[6:8]
alarm_period = alarmTime[9:].upper()        
now = datetime.now()                 #comparing current time with user-provided time
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")
if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound('C:\Users\Anika\Downloads\13767_morning_alarm.mp3')  #playsound() will play an MP3 file if user pass it the exact path
                    
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Get Up!!!")
                    playsound('C:\Users\Anika\Downloads\13767_morning_alarm.mp3')
                    break                