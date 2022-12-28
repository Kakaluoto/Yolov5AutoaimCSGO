python detect.py --weights runs/train/exp/weights/best.pt --source data/tuna_dataset/test_videos/tuna_test_video.mp4 --device 0 --save-txt
python detect.py --weights runs/train/exp/weights/best.pt --source data/tuna_dataset/test_images/right/ --device 0 --save-crop
python detect.py --weights runs/train/noise_yolov5m/weights/best.pt --source data/lowlight/bignoise/test --device 0 --conf-thres 0.3 --iou-thres 0.45
python detect.py --weights runs/train/noise_yolov5m/weights/best.pt --source data/lowlight/images --device 0 --conf-thres 0.3 --iou-thres 0.45 --save-crop
python detect.py --weights runs/train/noise_yolov5m/weights/best.pt --source data/lowlight/bignoise/test --device 0 --conf-thres 0.3 --iou-thres 0.45 --save-crop
python detect.py --weights runs/train/noise_yolov5m/weights/best.pt --source data/lowlight/bignoise/test --device 0 --conf-thres 0.3 --iou-thres 0.5
python detect.py --weights runs/train/noise_yolov5m/weights/best.pt --source data/lowlight/true_color --device 0 --conf-thres 0.3 --iou-thres 0.5 --save-txt --save-conf
python detect.py --weights runs/train/csgo/weights/best.pt --source data/csgo_data/video/csgo_aim_train_1.mp4 --device 0 --view-img