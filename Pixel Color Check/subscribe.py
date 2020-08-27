import pyautogui
import time

p = pyautogui.locateOnScreen (r'C:\Users\User\Desktop\Project\Phyton\images\serialnum.png', grayscale = True) #locate serial number box
pyautogui.click(p) #click serial number box
time.sleep(10) # wait 10 seconds

q = pyautogui.locateOnScreen (r'C:\Users\User\Desktop\Project\Phyton\images\pass.png') #locate pass button
pyautogui.click(q) #click pass button