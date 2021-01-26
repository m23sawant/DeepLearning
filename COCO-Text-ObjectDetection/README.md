

## Task:
To train an object detection neural network on COCO-Text dataset. Please read the ReadMe.pdf in Findings folder for detailed information. 
## File Structure:
~~~~~~~
        MayureshSawant
          |-- Findings
                |-- ReadMe.pdf
          |-- Models
                |-- best.pt
          |-- Research
                |-- COCO-Text.ipynb                
          |-- Scripts
                |-- coco_text.py
                |-- text.yaml          
          |-- README
~~~~~~~
## Setup Instructions:
1. First download the YOLOv5 repo and install the dependencies using:
 ~~~~~~~
!git clone https://github.com/ultralytics/yolov5 # clone repo
!pip install -qr yolov5/requirements.txt # install dependencies (ignore errors)
~~~~~~~
2. To make inference on an image or a video:
 ~~~~~~~
!python 'yolov5/detect.py' --weights '/MayureshSawant/Models/best.pt' --img 416 --conf 0.4 --source 'Location of image/video'
 ~~~~~~~