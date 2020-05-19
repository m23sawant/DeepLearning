# DeepLearning
A collection of my projects using Deep Learning and Neural Networks

* ## Computer Vision
1. ### Armored Superhero

| Dataset | Architecture | Transformations | Epochs | Time to train | Metrics |
| ------ | ------ | ------ | ------ | ------ | ------ | 
| Custom dataset from Bing Image Search API. 150 images for each Iron Man, War Machine and Iron Pariot | Resnet18 | Default augmentations in Fastai2 | 4 | 50s | Error Rate= 0.0952 |

2. ### Food 101

| Dataset | Architecture | Transformations | Epochs | Time to train | Metrics |
| ------ | ------ | ------ | ------ | ------ | ------ | 
| [Food-101](http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz) | Resnet50 | Default augmentations in Fastai2 + MixUp | 15 | 8 hours 15 minutes | Accuracy = 89.22% Top 5 accuracy = 98.17% |
