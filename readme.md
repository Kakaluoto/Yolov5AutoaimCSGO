# yolov5 CSGO 自动瞄准

整个基于yolov5项目，[ultralytics/yolov5: YOLOv5 🚀 in PyTorch > ONNX > CoreML > TFLite (github.com)](https://github.com/ultralytics/yolov5)

屏幕抓取调用win32

鼠标控制调用pynput

目录csgo_utils存放了屏幕抓取,鼠标控制的代码。

csgo_detect.py为检测脚本

执行脚本命令：
`python csgo_detect.py --weights runs/train/csgo/weights/best.pt --device 0 --view-img`

+ --view-img 参数可选，用于显示检测结果
+ --weights 参数指定使用权重
+ --device 0 选择使用哪块显卡