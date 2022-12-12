import datetime
import time
alarmTime = int(input("Set Time:"))
alarmAmPm = str(input("am/pm: "))
alarmDay = str(input("Choose Repeat days: "))
alarmName = str(input("Set Alarm Name: "))
alarmSnoozeTime = int(input("Snooze Time: "))
#alarmSound = str(input("Set Alarm Ringtone: "))
alarmVibration = str(input("Choose Vibration Mode: "))
alarmTurnOffOptions = str(input("Choose Optopns: "))
def validate_time(alarmTime):
    if len(alarmTime) != 11:
        return "Invalid time format! Please try again..."
    
    else:
            return "ok"
