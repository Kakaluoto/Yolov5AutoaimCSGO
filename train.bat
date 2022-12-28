python train.py --data lowlight.yaml --cfg lowlight_yolov5m.yaml --weights weights/yolov5m.pt --epochs 1000 --batch-size 32
python train.py --data lowlight.yaml --cfg lowlight_yolov5l.yaml --weights weights/yolov5l.pt --imgsz 800 --epochs 1000 --batch-size 16
python train.py --data lowlight.yaml --cfg lowlight_yolov5l.yaml --weights weights/yolov5l.pt --epochs 1000 --batch-size 32
python train.py --data lowlight.yaml --cfg lowlight_yolov5m.yaml --weights weights/yolov5m.pt --imgsz 800 --epochs 1000 --batch-size 32
python train.py --data csgo.yaml --cfg csgo_yolov5m.yaml --weights weights/yolov5m.pt --epochs 3000 --batch-size 4
