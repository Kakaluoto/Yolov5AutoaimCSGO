# coding=utf-8
import pynput
import numpy as np
from pynput.mouse import Listener, Button, Controller
import ctypes

PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)


class MouseController:
    def __init__(self):
        self.lock_mode = False
        self.mouse = Controller()

    def on_click(self, x, y, button, is_press):
        print(f"鼠标{button}键在({x}, {y})处{'按下' if is_press else '松开'}")
        if button == Button.x2 and is_press:
            self.lock_mode = not self.lock_mode
        # else:
        #     self.lock_mode = False
        if button == Button.right:
            return False

    def start_listen(self):
        # with Listener(on_click=self.on_click) as listener:
        #     listener.join()
        listener = Listener(on_click=self.on_click)
        listener.start()

    def lock_on(self, target_center_list=None):
        mouse_xy = np.array(self.mouse.position)
        l2_distance = np.sum((target_center_list - mouse_xy) ** 2, axis=1)
        index = np.argmin(l2_distance)
        closest_point = target_center_list[index]
        self.mouse.position = (int(closest_point[0]), int(closest_point[1]))
        # dx, dy = int(closest_point[0]) - mouse_xy[0], int(closest_point[1]) - mouse_xy[1]
        # self.mouse.move(dx, dy)

        print('The current pointer position is {0}'.format(
            self.mouse.position))


if __name__ == "__main__":
    mouse_controller = MouseController()
    mouse_controller.lock_on()
