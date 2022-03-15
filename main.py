import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api

from win32gui import FindWindow, GetWindowRect
from random import randint

# FindWindow takes the Window Class name (can be None if unknown), and the window's display text.
# window_handle = FindWindow(None, "pygame window")
window_handle = FindWindow(None, "Stay in Queue - YouTube — Личный: Microsoft​ Edge")

monitorInfo = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
screen_image = np.array(ImageGrab.grab())

w_factor = len(screen_image[0]) / monitorInfo['Monitor'][2]
h_factor = len(screen_image) / monitorInfo['Monitor'][3]

ok = 0

while True:
    time.sleep(0.1)
    window_rect = GetWindowRect(window_handle)
    # print(window_rect)
    dx, dy, w, h = window_rect
    # cx, cy = win32api.GetCursorPos()
    # cx = round(cx * 1.25)
    # cy = round(cy * 1.25)
    # print(cx, cy)
    # cx = round(cx * w_factor)
    # cy = round(cy * h_factor)
    # cx = dx + 960
    # cy = dy + 80
    cx = dx + 230 + randint(-10, 10)
    cy = dy + 450
    screen_image = ImageGrab.grab(bbox=[cx, cy, cx + 1, cy + 1])
    # print(screen_image)
    p_color = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2RGBA)
    # if (p_color[0][0][0], p_color[0][0][1], p_color[0][0][2]) != (0, 0, 0):
    #     print(cx, cy, p_color[0][0][0], p_color[0][0][1], p_color[0][0][2])
    if p_color[0][0][2] > 200:
        ok = 0
        print(cx, cy, p_color[0][0][2])
    else:
        ok += 1
        if ok > 5:
            print('ok')
        else:
            print('.', end='')

# 37 157 - начало очереди
# 746 157 - середина очереди

# 255 206 150
# 235 190 138

# 149 - 318 y 449
# 644 - 806 y 462

# настроить подсчёт обеих очередей и вывод по каждой