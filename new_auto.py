import threading
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import cv2
import numpy as np
import pyautogui

total_time = 0
def finished():

    found = driver.find_element_by_id('video_longest_frame').text
    if(found == None or found == ''):
        finished()
    else:
        print(found)
        print("found")
        return 1


urls = ["https://ghost.sk/upwork/params-2024-total/video.php?latitude=38.5&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear",
"https://ghost.sk/upwork/params-2024-total/video.php?latitude=37.18108&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear"
,"https://ghost.sk/upwork/params-2024-total/video.php?latitude=39&longitude=86&zoom=4&time=min&inset_width=200&inset_height=150&inset_sun=100&inset2_width=200&inset2_height=150&inset2_sun=30&fps=10&video_controls=on&tz=GMT&tz_offset=0&video_intro=5&video_outro=5&lang=en&offset1=40&offset_mid=0.1&dur_a=0.15&dur_b=5&s3v_a=0.25&s2v_a=0.1&location=Franklin%2C%20IN&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0"    
]

options = Options()

for url in urls:

    options.add_argument('start-maximized')

    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    pyautogui.press('f11')
    driver.get(url)

    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1366,786))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            if finished():
                break
        else:
            print('What!?')
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f'Finished')
    driver.quit()
    break