# import numpy as np
# from PIL import ImageGrab
# import cv2
# import time
# import win32api
#
# from win32gui import FindWindow, GetWindowRect
# from random import randint
#
# # FindWindow takes the Window Class name (can be None if unknown), and the window's display text.
# # window_handle = FindWindow(None, "pygame window")
# window_handle = FindWindow(None, "Stay in Queue - YouTube — Личный: Microsoft​ Edge")
#
# monitorInfo = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
# screen_image = np.array(ImageGrab.grab())
#
# w_factor = len(screen_image[0]) / monitorInfo['Monitor'][2]
# h_factor = len(screen_image) / monitorInfo['Monitor'][3]
#
# ok = 0
#
# length_queue = []
# bears_y = [620, 610, 536, 458, 388, 305]
#
# while True:
#     time.sleep(0.1)
#     window_rect = GetWindowRect(window_handle)
#     # print(window_rect)
#     dx, dy, w, h = window_rect
#     # cx, cy = win32api.GetCursorPos()
#     # cx = round(cx * 1.25)
#     # cy = round(cy * 1.25)
#     # print(cx, cy)
#     # cx = round(cx * w_factor)
#     # cy = round(cy * h_factor)
#     # cx = dx + 960
#     # cy = dy + 80
#     length_queue = 0
#     for i in range(len(bears_y)):
#         cx = dx + 230 #+ randint(-5, 5)
#         cy = dy + bears_y[i]
#         screen_image = ImageGrab.grab(bbox=[cx, cy, cx + 1, cy + 1])
#         # print(screen_image)
#         p_color = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2RGBA)
#         # if (p_color[0][0][0], p_color[0][0][1], p_color[0][0][2]) != (0, 0, 0):
#         #     print(cx, cy, p_color[0][0][0], p_color[0][0][1], p_color[0][0][2])
#         if p_color[0][0][2] > 200:
#             length_queue += 1
#             if i > length_queue:
#                 length_queue = i
#             ok = 0
#             print(cx, cy, p_color[0][0][2])
#         else:
#             ok += 1
#             if ok > 5:
#                 print('ok')
#             else:
#                 print('.', end='')
#         print(length_queue)
#
# # 37 157 - начало очереди
# # 746 157 - середина очереди
#
# # 255 206 150
# # 235 190 138
#
# # 149 - 318 y 449
# # 644 - 806 y 462
#
# # настроить подсчёт обеих очередей и вывод по каждой


import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api, win32gui

from win32gui import FindWindow, GetWindowRect
from random import randint


def callback(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        print(f"window text: '{win32gui.GetWindowText(hwnd)}'")


win32gui.EnumWindows(callback, None)

# FindWindow takes the Window Class name (can be None if unknown), and the window's display text.
# window_handle = FindWindow(None, "pygame window")
window_handle = FindWindow(None, "Stay in Queue - YouTube — Личный: Microsoft​ Edge")

monitorInfo = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
screen_image = np.array(ImageGrab.grab())

w_factor = len(screen_image[0]) / monitorInfo['Monitor'][2]
h_factor = len(screen_image) / monitorInfo['Monitor'][3]

ok = 0

length_queue = []
left_queue = {
    'x': (115, 240),
    'y': (245, 604),
    'p': (40, 40)  # precision
}

print(left_queue)


def isBear(x, y):
    print(x, y, end='')
    screen_image = ImageGrab.grab(bbox=[cx, cy, cx + 1, cy + 1])
    # print(screen_image)
    p_color = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2RGBA)
    if p_color[0][0][2] > 200:
        print('bear')
        return True
    else:
        print('')
    return False


# with_cursor = True
with_cursor = False

while True:
    time.sleep(0.1)
    window_rect = GetWindowRect(window_handle)
    dx, dy, w, h = window_rect
    length_queue = 0

    for qy in range(left_queue['y'][1] - 150, left_queue['y'][0], -left_queue['p'][0]):
        i = 1
        for qx in range(left_queue['x'][0], left_queue['x'][1], left_queue['p'][1] // 2):
            qx -= left_queue['x'][0]
            i = -i
            if with_cursor:
                cx, cy = win32api.GetCursorPos()
                cx = round(cx * w_factor)
                cy = round(cy * h_factor)
            else:
                center_qx = (left_queue['x'][1] - left_queue['x'][0]) // 2 + left_queue['x'][0]
                cx = dx + center_qx + qx * i  # + randint(-5, 5)
                cy = dy + qy
            if isBear(cx, cy):
                length_queue += 1
                break
        if (length_queue > 0):
            break

    if(length_queue > 0):
        print('queue too long!')