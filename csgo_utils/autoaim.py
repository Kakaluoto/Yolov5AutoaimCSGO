# coding=utf-8
import pynput
import numpy as np
from pynput.mouse import Listener, Button, Controller
import ctypes

PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)


# 鼠标控制器

class MouseController:
    def __init__(self):
        self.lock_mode = False
        self.mouse = Controller()

    def on_click(self, x, y, button, is_press):
        # print(f"鼠标{button}键在({x}, {y})处{'按下' if is_press else '松开'}")
        # 使用鼠标的侧键来开关自动跟枪的状态
        if button == Button.x2 and is_press:
            self.lock_mode = not self.lock_mode
        # 使用鼠标右键直接退出跟踪状态
        if button == Button.right:
            return False

    def start_listen(self):
        # with Listener(on_click=self.on_click) as listener:
        #     listener.join()
        listener = Listener(on_click=self.on_click)
        listener.start()

    # 控制鼠标移动到最近的检测框中心点
    def lock_on(self, target_center_list=None):
        # 获取鼠标的坐标
        mouse_xy = np.array(self.mouse.position)
        # 计算鼠标坐标和所有检测框中心点的L2范数(即欧氏距离)
        l2_distance = np.sum((target_center_list - mouse_xy) ** 2, axis=1)
        # 找到距离最小的检测框的下标索引
        index = np.argmin(l2_distance)
        # 根据距离最小的检测框的下表找到对应的检测框
        closest_point = target_center_list[index]
        # 通过将距离最小的检测框的中心坐标赋值给mouse.position来移动鼠标
        self.mouse.position = (int(closest_point[0]), int(closest_point[1]))

        # print('The current pointer position is {0}'.format(
        #     self.mouse.position))


if __name__ == "__main__":
    mouse_controller = MouseController()
    mouse_controller.lock_on()
