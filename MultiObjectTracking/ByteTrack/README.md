# SORT Multi-Object Tracking for HA-ViD.
This repository has been adapted from the original [ByteTrack](https://github.com/ifzhang/ByteTrack), [SORT](https://github.com/abewley/sort), and [IKEA_ASM](https://github.com/IkeaASM/IKEA_ASM_Dataset/tree/master/part-tracking) repositories.

## Dependencies:
This code makes use of the following packages:
1. [`scikit-learn`](http://scikit-learn.org/stable/)
2. [`scikit-image`](http://scikit-image.org/download)
3. [`FilterPy`](https://github.com/rlabbe/filterpy)
4. ['ByteTrack'](https://github.com/ifzhang/ByteTrack)

## 1. Generate ground truth tracklets
* Generate ground truth tracklets from the annotation file. Each time, take one video annotation file as input. 
* Run `python get_tracking_gt.py -f [path to annotation file]`
* You will get a `tracking_gt.txt` file, and it will be used for evaluation.

## 2. Convert object detection results
This step is to convert the object detection results to a proper format for tracking.
* Get object detection results from [Object Detection] repository. Each time, take one video as input. The result is a `.pkl` file.
* Convert detection results format by running  `python get_dets_from_pkl.py -f [path to the detection result .pkl file]`
* You will get a `dets.txt` file.

## 3. Tracking objects
This step takes `dets.txt` as input, and leverages SORT algorithm to track detected objects.
* Run `python ByteTrack.py -f [path to dets.txt file]`
* You will get a `tracklets.txt` file

## 4. Evaluation
This step evaluates the tracking results.
* Run `python eval.py -gt [path to the ground truth file] -tr [path to the tracking result file]` 
* We report MOTA, IDF1, ML, MT, IDS results.

## 5. Convert object annotation to detection result format
We want to use ground truth object bboxes to test SORT tracking performance. This step is to convert object annotation file to the detection result format for tracking.
* Run step 1 to get `tracking_gt.txt` file.
* Run `python get_dets_from_gt.py -f [path to the tracking_gt.txt file]`
* You will get a `dets_gt.txt` file.

## 6. Tracking and evaluation on ground truth detection
* Run `python ByteTrack.py -f [path to dets_gt.txt file]`
* Run `python eval.py -gt [path to the tracking_gt.txt file] -tr [path to the dets_gt.txt file]`

## 7. Visualization
We use the visulization tool provided by [IKEA_ASM](https://github.com/IkeaASM/IKEA_ASM_Dataset/tree/master/part-tracking) to visulize tracking results.
* Run `python visualize_tracker.py -s [path to the tracking result file tracklets.txt] -root [path to the folder containing images of the tracked video]`
* You will get the images with tracking results in the folder `outputs/tracking_results`

## Acknowledgement
We appreciate the collaborators/maintainers of the [SORT](https://github.com/abewley/sort) and [IKEA_ASM](https://github.com/IkeaASM/IKEA_ASM_Dataset/tree/master/part-tracking) repositories.

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License, found here. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.
