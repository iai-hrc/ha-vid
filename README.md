# [HA-ViD](https://github.com/iai-hrc/ha-vid): A Human Assembly Video Dataset for Comprehensive Assemby Knowledge Understanding
![model](https://github.com/iai-hrc/iai-hrc.github.io/blob/main/assets/Fig1.png)

HA-ViD – the first human assembly video dataset that features representative industrial assembly scenarios, natural procedural knowledge acquisition process, and consistent human-robot shared annotations. Specifically, HA-ViD captures diverse collaboration patterns of real-world assembly, natural human behaviors and learning progression during assembly, and granulate action annotations to
subject, action verb, manipulated object, target object, and tool. We provide 3222 multi-view, multi-modality videos (each video contains one assembly task), 1.5M frames, 96K temporal labels and 2M spatial labels.

# Overview
This repository contains links for downloading the data and codes for benchmarking algorithms of Action Recognition, Action Segmentation, Object Detection and Multi-Object Tracking.

The data is hosted in Dropbox. Please submit an access request from [Our Website](https://iai-hrc.github.io/ha-vid).

## Folder structure of HA-ViD data
The `data` folder is:
```
data
├── view0_lh_pt
│   ├──
├── ActionRecognition
│   ├── mmskeleton
├── ActionSegmentation
│   ├── data
│   │   ├── features
│   │   ├── view0_lh_aa
│   │   │   ├── groundTruth
│   │   │   ├── splits
│   │   │   ├── mapping.txt
│   │   ├── view0_lh_pt
│   │   │   ├── ...
│   │   ├── ...
├── ObjectDetection
│   ├── train
│   │   ├── annotations
│   │   ├── images
│   ├── val
│   │   ├── annotations
│   │   ├── images
├── PretrainedCheckpoints
│   ├── ActionRecognition
│   │   ├── i3d_flow
│   │   ├── i3d_rgb
│   │   ├── mvit
│   │   ├── st_gcn
│   │   ├── timesformer
│   ├── ActionSegmentation
│   │   ├── BCN
│   │   │   ├── bcn_models
│   │   │   ├── bgm_models
│   │   ├── DTGRM
│   │   ├── ms-tcn
│   ├── ObjectDetection
│   │   ├── dino
│   │   ├── faster_rcnn_r50
│   │   ├── faster_rcnn_r101
│   │   ├── faster_rcnn_x101
│   │   ├── yolov5_l
│   │   ├── yolov5_s
```
`data` contains the raw data, including rgb videos, depth videos and skeleton data, the annotated data for three tasks, including Action Recognition, Action Segmentation, and Object Detection, and the checkpoints of the pretrained models for the three tasks. 



## Citation
If you find our code useful, please cite our paper. 
```
@inproceedings{
  author    = {Hao Zheng and
               Regina Lee and
               Yuqian Lu},
  title     = {HA-ViD: Human Assembly Video Dataset for Comprehensive Assembly Knowledge Understanding},
  journal = {}
}
```

## Acknowledgement

This work was supported by The University of Auckland FRDF New Staff Research Fund (No.3720540).

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.

## Code of Conduct
Code of Conduct of HA-ViD can be found in [Our Website](https://iai-hrc.github.io/ha-vid).