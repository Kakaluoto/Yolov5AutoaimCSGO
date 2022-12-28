python val.py --weights runs/train/noise_yolov5m/weights/best.pt --data lowlight.yaml --conf-thres 0.3 --iou-thres 0.45 --task test
python val.py --weights runs/train/noise_yolov5m/weights/best.pt --data lowlight.yaml --conf-thres 0.3 --iou-thres 0.5 --task test
python val.py --weights runs/train/noise_yolov5m/weights/best.pt --data lowlight.yaml --conf-thres 0.3 --iou-thres 0.7 --task test
python val.py --weights runs/train/fake_color_yolov5m_size_640/weights/best.pt --data lowlight.yaml --conf-thres 0.3 --iou-thres 0.45 --task test
python val.py --weights runs/train/fake_color_yolov5m_size_640/weights/best.pt --data lowlight.yaml --conf-thres 0.3 --iou-thres 0.45 --task train
python val.py --weights runs/train/fake_color_yolov5m_size_640_clear_added/weights/best.pt --data lowlight.yaml --conf-thres 0.3 --iou-thres 0.45 --task test