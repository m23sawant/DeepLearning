# DeepLearning
A collection of my projects using Deep Learning and Neural Networks

* ## Computer Vision
1. ### [Armored Superhero](https://github.com/mayuresh23sawant/DeepLearning/tree/master/ArmoredSuperhero)

| Dataset | Architecture | Transformations | Epochs | Time to train | Metrics |
| ------ | ------ | ------ | ------ | ------ | ------ | 
| Custom dataset from Bing Image Search API. 150 images for each Iron Man, War Machine and Iron Pariot | Resnet18 | Default augmentations in Fastai2 | 4 | 50s | Error Rate= 0.0952 |

2. ### [Food 101](https://github.com/mayuresh23sawant/DeepLearning/tree/master/Food-101)

| Dataset | Architecture | Transformations | Epochs | Time to train | Metrics |
| ------ | ------ | ------ | ------ | ------ | ------ | 
| [Food-101](http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz) | Resnet50 | Default augmentations in Fastai2 + MixUp | 15 | 8 hours 15 minutes | Accuracy = 89.33% Top 5 accuracy = 98.17% |

2. ### [Food 101](https://github.com/m23sawant/DeepLearning/tree/master/COCO-Text-ObjectDetection)

| Dataset | Architecture | Transformations | Epochs | Time to train | Metrics |
| ------ | ------ | ------ | ------ | ------ | ------ | 
| [COCO-Text](https://bgshih.github.io/cocotext/) | YOLOv5 | Mosiac | 20 | 3 hours 40 minutes | Precision: 0.34, Recall: 0.704, mAP@0.5: 0.58, mAP@0.95: 0.265 |
