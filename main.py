import cv2
import numpy as np
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import pyautogui
import webbrowser
import time
import sys


def clear_console():
    os.system('cls')

clear_console()

sys.setrecursionlimit(10**6) 



def finished():

    found = driver.find_element_by_id('video_longest_frame').text
    if(found == None or found == ''):
        return 0
    else:
        print(found)
        print("found")
        return 1

all_urls = ["https://ghost.sk/upwork/params-2024-total/video.php?latitude=38.5&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear",
"https://ghost.sk/upwork/params-2024-total/video.php?latitude=37.18108&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear",
"https://ghost.sk/upwork/params-2024-total/video.php?latitude=39&longitude=86&zoom=4&time=min&inset_width=200&inset_height=150&inset_sun=100&inset2_width=200&inset2_height=150&inset2_sun=30&fps=10&video_controls=on&tz=GMT&tz_offset=0&video_intro=5&video_outro=5&lang=en&offset1=40&offset_mid=0.1&dur_a=0.15&dur_b=5&s3v_a=0.25&s2v_a=0.1&location=Franklin%2C%20IN&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0"]

urls = ["https://ghost.sk/upwork/params-2024-total/video.php?latitude=38.5&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear",
"https://ghost.sk/upwork/params-2024-total/video.php?latitude=37.18108&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear"]

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
options = Options()
id = 0
pyautogui.FAILSAFE = False

for url in urls:

    if driver:
         driver.quit()
         
    options.add_argument('start-maximized')

    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    # driver = webdriver.Chrome(path)

    pyautogui.press('f11')
    driver.get(url)


    id = id + 1 

    output = f'city_id={id}.avi'
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    #get info from img
    height, width, channels = img.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

    i = 0
    while i < 1 :
        img = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(image)
        if driver.find_element_by_id('video_longest_frame').text != "": 
            i = 2
       
    print(f'Finished city_id={id}')
    out.release()
    cv2.destroyAllWindows()
    driver.quit()
