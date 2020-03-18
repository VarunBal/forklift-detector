# Forklift-detector

CNN model to detect a forklift in a webcam stream in realtime using YOLOV3 algorithm 
based on Darknet framework trained on Google Colab platform.

## Data Gathering

Images were scrapped from 3 sources.

1. Downloaded from Imagenet’s ‘forklift’ synset.
2. Scraped from Google images search.
2. Scraped from Flickr images search. 

In total 5124 images were collected.

## Data Cleaning

The data was cleaned by manually removing the unwanted images 
from all the sources that could potentially affect the accuracy of detection. 

After cleaning 1876 data samples remained.

## Model Selection

#### YoloV3
 
The YOLO algorithm for object detection was selected for its speed to be implemented 
in real-time applications for fast detection and its performance while being deployed 
on low powered systems.

More details: http://pjreddie.com/darknet/yolo/

## Data Labelling

The all of the 1876 data samples were labelled.

![Image](Screencaps/labelling.png?raw=true)

This gives ‘.txt’ label file for each 
training sample. In the format:

```
<class_id> <xc> <yc> <width> <height> 
```

Where ‘class_id’ is the label of the class the object belongs to, xc, yc, width, 
height are centre coordinates, width and height of the boundary box respectively.

![Image](Screencaps/labeling_txt.JPG?raw=true) 

## Model Training 
 
The model was trained on google colab’s dedicated GPU instance with input size 
of 416 x 416 pixels for 4000 iterations. 
 
## Model Evaluation 
 
The Mean Average Precision (MaP) of the model was calculated to be 69.32%. The 
average Intersection over union (IOU) of detection and ground truth is calculated 
to be 71.21%

![Image](Screencaps/model_map.JPG?raw=true) 

## Detection 

The speed of detection is fast and real time with over 45fps. 

#### Sample detections:

###### Kindly see the attached video for reference of real time detection.

![Image](results/predictions_1.jpg?raw=true)
![Image](results/predictions_2.jpg?raw=true)
![Image](results/predictions_3.jpg?raw=true)
![Image](results/predictions_4.jpg?raw=true)
![Image](results/predictions_5.jpg?raw=true)

## Model Improvements 
Given the time, the detection accuracy of the model can be improved upon by:

* Increasing the resolution of the input layer of the model from 416 x 416, so the 
smaller objects can be detected and the detection of false positives can be minimised.
* Training for more iterations to better fit the model to the training data to improve 
detection accuracy.
* Gathering more data samples if possible.