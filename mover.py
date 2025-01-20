import Quartz
import time
import pyautogui

pyautogui.FAILSAFE = False

def getIdleTime():
    idle = Quartz.CGEventSourceSecondsSinceLastEventType(Quartz.kCGEventSourceStateHIDSystemState, Quartz.kCGAnyInputEventType)
    return idle

def pressShift():
    while getIdleTime() > 240:
        pyautogui.press('shift')
        time.sleep(5)

while True:
    if getIdleTime() > 240:
        pressShift()
    time.sleep(30)