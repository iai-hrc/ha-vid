# Object Detection
This explain how to benchmark Object Detection of HA-ViD.

We use [MMDetection](https://github.com/open-mmlab/mmdetection) and [mmyolo] (https://github.com/open-mmlab/mmyolo), two open source object detection toolboxes based on Pytorch, to benchmark FasterRCNN, DINO, and YOLOv5 on HA-ViD.

## Prepare Datasets 
Download the dataset from ..., and put dataset in subfolder `data`.

The `data` folder structure should be:

```
data
├── train
│   ├── annotations
│   ├── images
├── val
│   ├── annotations
│   ├── images

```
`data` folder contains two subfolders `train` and `val`, and each subfolder contains a folder 'annotations' containing `.json` annotation file and a folder `images` containing all the raw `.PNG` images.

## Implement MMDetection and mmyolo
[openmmlab](https://openmmlab.com/) provides easy-to-implement object detection toolboxes. That's why we don't provide the source codes for [MMDetection](https://github.com/open-mmlab/mmdetection) and [mmyolo] (https://github.com/open-mmlab/mmyolo).
* To implement MMDetection, please refer to the official github repository [MMDetection](https://github.com/open-mmlab/mmdetection).
* To implement mmyolo, please refer to the official github repository [mmyolo] (https://github.com/open-mmlab/mmyolo).

## Configs
Instead of providing source codes of [MMDetection](https://github.com/open-mmlab/mmdetection) and [mmyolo] (https://github.com/open-mmlab/mmyolo), we provide the configure files for each model.

Configure files are stored in the subfolder `configs`

After implementing MMDetection and mmyolo repositories, put the configure files in the `configs` folder of MMDetection and mmyolo.

## Checkpoints
We provide the pretrained checkpoints for each model in the folder `checkpoints`.

After implementing MMDetection and mmyolo repositories, put the checkpoint files in the `checkpoints` folder of MMDetection and mmyolo.

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

We appreciate the collaborators/maintainers of the [MMDetection](https://github.com/open-mmlab/mmdetection) and [mmyolo] (https://github.com/open-mmlab/mmyolo).

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License, found here. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.