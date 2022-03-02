import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api

while True:
    time.sleep(0.1)
    cx, cy = win32api.GetCursorPos()
    cy += 20
    # print(cx, cy)
    screen_image = np.array(ImageGrab.grab(bbox=[cx, cy, cx + 1, cy + 1]))
    p_color = screen_image  # cv2.cvtColor(screen_image, cv2.COLOR_BGR2RGB)
    print(cx, cy, p_color[0][0][0], p_color[0][0][1], p_color[0][0][2])

# 37 157 - начало очереди
# 746 157 - середина очереди

#*