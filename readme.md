# yolov5 CSGO 自动瞄准
## 1. 说明

整个基于yolov5项目，[ultralytics/yolov5: YOLOv5 🚀 in PyTorch > ONNX > CoreML > TFLite (github.com)](https://github.com/ultralytics/yolov5)

目前只能支持游戏全屏窗口化，不支持全屏和其他分辨率的窗口化。

游戏全屏或者不以最大分辨率窗口化均会导致检测失败，暂时还没解决。。。。。。

屏幕抓取调用win32

鼠标控制调用pynput

目录`csgo_utils`存放了屏幕抓取,鼠标控制的代码

`grab_screen.py`负责抓取屏幕

`autoaim.py`负责控制鼠标

`csgo_detect.py`为检测脚本

## 2. 使用方式

执行脚本命令：
`python csgo_detect.py --weights runs/train/csgo/weights/best.pt --device 0 --view-img`

+ --view-img 参数可选，用于显示检测结果，建议不选
+ --weights 参数指定使用权重
+ --device 0 选择使用哪块显卡

执行脚本后，点击鼠标侧键开启锁定模式，再次点击关闭锁定模式，点击鼠标右键直接退出。

需要修改对应按键的，直接修改autoaim.py的on_click函数

```python
def on_click(self, x, y, button, is_press):
    # print(f"鼠标{button}键在({x}, {y})处{'按下' if is_press else '松开'}")
    # 使用鼠标的侧键来开关自动跟枪的状态
    if button == Button.x2 and is_press:
        self.lock_mode = not self.lock_mode
    # 使用鼠标右键直接退出跟踪状态
    if button == Button.right:
        self.flag = False
```

