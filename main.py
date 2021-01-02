import cv2
import numpy as np
import os
import pyautogui
import webbrowser
import time
# from pynput.keyboard import Key, Controller

# keyboard = Controller()
ids = [4,5,6]
for id in ids:
   
    webbrowser.open(f'http://sandbox.eclipse2024.org/eclipse-simulator/2024/index.html?city_id={id}')  # Go to example.com   # keyboard.press('f11')
    # keyboard.release('f11')
    if(id==4):  
        time.sleep(1)
        pyautogui.press('f11')
        time.sleep(15)
    else:
        time.sleep(15)
    
    output = f'city_id={id}.avi'
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    #get info from img
    height, width, channels = img.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

    for i in range(95):
        img = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(image)
        StopIteration(10)
       
    print(f'Finished city_id={id}')
    out.release()
    cv2.destroyAllWindows()