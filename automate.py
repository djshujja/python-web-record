import threading
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import cv2
import numpy as np
import pyautogui


# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t

total_time = 0
def finished():
    # done = driver.find_element_by_xpath('/html/body/div[3]/span[2]')
    # print('Looking')
    # print(sec)
    found = driver.find_element_by_id('video_longest_frame').text
    if(found == None or found == ''):
        finished()
    else:
        print(found)
        print("found")
        return 1
    # try:
    #     print("Found")
    #     return 
    #     # return driver.find_element_by_id('video_s').text
    # except:
    #     finished()
    # return done

urls = ["https://ghost.sk/upwork/params-2024-total/video.php?latitude=38.5&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear",
"https://ghost.sk/upwork/params-2024-total/video.php?latitude=37.18108&longitude=91.62261&zoom=7&time=min&inset_width=350&inset_height=350&inset_sun=310&inset2_width=250&inset2_height=250&inset2_sun=65&fps=24&video_controls=on&tz=CDT&tz_offset=-5&video_intro=1&video_outro=1&lang=en&offset1=45&offset_mid=0.12&dur_a=0.15&dur_b=5&s3v_a=0.1&s2v_a=0.1&location=City%2C%20ST&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0&thermometer=linear"
,"https://ghost.sk/upwork/params-2024-total/video.php?latitude=39&longitude=86&zoom=4&time=min&inset_width=200&inset_height=150&inset_sun=100&inset2_width=200&inset2_height=150&inset2_sun=30&fps=10&video_controls=on&tz=GMT&tz_offset=0&video_intro=5&video_outro=5&lang=en&offset1=40&offset_mid=0.1&dur_a=0.15&dur_b=5&s3v_a=0.25&s2v_a=0.1&location=Franklin%2C%20IN&scene=field4&corona=round1&show_speed=on&in_window=on&width=2160&height=1215&offset_x=0"    
]
fuu = 0
options = Options()

for url in urls:
    fuu+1
    # webbrowser.open(f'http://sandbox.eclipse2024.org/eclipse-simulator/2024/index.html?city_id={id}')  # Go to example.com   # keyboard.press('f11')
    # keyboard.release('f11')
    options.add_argument('start-maximized')
    # options.add_argument('disable-infobars')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    pyautogui.press('f11')
    driver.get(url)

#    set_interval()

    
    
    

    output = f'city_id=done.avi'
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    #get info from img
    height, width, channels = img.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

    while True:
        img = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(image)
        finished()
        break
        
    print(f'Finished')
    out.release()
    cv2.destroyAllWindows()
    driver.quit()
    break