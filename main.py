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
    'p': (5, 5),  # precision
    'b_s': ()
}
b_s_y = (left_queue['y'][1] - left_queue['y'][0]) // 7
left_queue['b_s'] = (b_s_y, b_s_y)

print(left_queue)


def isBear(x, y, p_color):
    # print(x, y, end='')
    if len(p_color) - 1 < y or len(p_color[0] - 1) < x:
        return False
    if p_color[y][x][2] > 200:
        # print('bear')
        return True
    # print('')
    return False


def queue_proc(queue_params):
    max_length_queue = length_queue = 0  #
    min_y = queue_params['y'][1]
    screen_image = ImageGrab.grab(bbox=[
        queue_params['x'][0] * w_factor,
        queue_params['y'][0] * h_factor,
        queue_params['x'][1] * w_factor,
        queue_params['y'][1] * h_factor
    ])
    p_color = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2RGBA)

    for qy in range(queue_params['y'][1], queue_params['y'][0], -queue_params['p'][0]):
        i = 1
        for qx in range(queue_params['x'][0], queue_params['x'][1], queue_params['p'][1]):
            qx -= queue_params['x'][0]
            i = -i
            if with_cursor:
                cx, cy = win32api.GetCursorPos()
                cx = round(cx * w_factor)
                cy = round(cy * h_factor)
            else:
                center_qx = (queue_params['x'][1] - queue_params['x'][0]) // 2 + queue_params['x'][0]
                cx = dx + center_qx + qx * i  # + randint(-5, 5)
                cy = dy + qy
            if isBear(cx - queue_params['x'][0], cy - queue_params['y'][0], p_color):
                length_queue += 1
                break
        if length_queue > 0:
            if length_queue > max_length_queue:
                max_length_queue = length_queue
                min_y = qy
    if length_queue > 0:
        # print('queue too long!')
        real_length_queue = queue_params['y'][1] - min_y
        print('Длина очереди равна: ', real_length_queue // queue_params['b_s'][1])


# with_cursor = True
with_cursor = False

while True:
    time.sleep(0.1)
    window_rect = GetWindowRect(window_handle)
    dx, dy, w, h = window_rect
    queue_proc(left_queue)
    queue_proc(right_queue)

# иcправить ошибки + очереди в цикл (вместо двух вызовов)
