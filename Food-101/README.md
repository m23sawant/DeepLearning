# Food-101
The Food-101 dataset is one of the most popular datasets in the world for food items. There are 101 food classes, each having 1000 images. For each class, the data is split as 750-250 into training and validation set. The dataset was first used in [Food-101 – Mining Discriminative Components with Random Forests](https://homes.esat.kuleuven.be/~konijn/publications/2014/bossard_eccv14_food-101.pdf) at the Computer Vision Lab, ETH Zurich.

### Current State of The Art Results
Back in 2014, when the paper was published, researchers could correctly classify the classes with an accuracy of 50.76% with Random Forests. The current State of the art results were acheived by [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/pdf/1905.11946v3.pdf) and [GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism.
](https://arxiv.org/abs/1811.06965) obtaining a top-1 accuracy of 93%.
### My Solution
I have not used specialized architectures or huge models, but something very simple. An off-the-shelf Resnet50 paired with Fast.ai. And as the founder of Fast.ai Jeremy Howard says, *Fast.ai will spread machine learning far beyond the select few practitioners who dominate the field.* Without using any custom architecture and by using free GPU resource like Google Colab, I was able to acheive near-SoTA results. This was possible mainly because of the use of image augmentations, progressive resizing and test time augmentations. 

Steps Involved:
1. Fetch the data from the url and extract it. 
2. Using the fastai datablock API to :
- Get the source items
- Split the items into the training set and one or more validation sets
- Label the items
- Processing the items (such as normalization, and augmentations)
- Collating the items into batches.
3. Create a learner object which will provide an abstraction combining an optimizer, a model, and the data to train it.
4. Fine tuning the model with transfer learning strting with small sized images
5. Progressiveliy increasing the size of images as the trainig goes on. 
6. Making inferences from the model using Test Time Augmentations
