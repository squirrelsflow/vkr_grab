import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api

from win32gui import FindWindow, GetWindowRect

# FindWindow takes the Window Class name (can be None if unknown), and the window's display text.
window_handle = FindWindow(None, "pygame window")

while True:
    time.sleep(0.1)
    window_rect = GetWindowRect(window_handle)
    # print(window_rect)
    dx, dy, w, h = window_rect
    # cx, cy = win32api.GetCursorPos()
    # cx = round(cx * 1.25)
    # cy = round(cy * 1.25)
    # print(cx, cy)
    cx = dx + 960
    cy = dy + 80
    screen_image = ImageGrab.grab(bbox=[cx, cy, cx + 1, cy + 1])
    # print(screen_image)
    p_color = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2RGBA)
    if (p_color[0][0][0], p_color[0][0][1], p_color[0][0][2]) != (0, 0, 0):
        print(cx, cy, p_color[0][0][0], p_color[0][0][1], p_color[0][0][2])



# 37 157 - начало очереди
# 746 157 - середина очереди

# *
