# Action Segmentation
This repository contains scripts and models for the Action Segmentation benchmark of HA-ViD.

We benchmark [MS-TCN](https://github.com/yabufarha/ms-tcn), [DTGRM](https://github.com/redwang/DTGRM), and [BCN](https://github.com/MCG-NJU/BCN) on HA-ViD.

## Prepare Datasets 
Download the data from ..., and put data in subfolder `data`.

The `data` folder structure should be:
```
data
├── view0_lh_pt
│   ├── features
│   ├── groundTruth
│   ├── splits
│   ├── mapping.txt
├── view0_lh_aa
│   ├── ...
...
```
`view0`, `view1`, `view2` denote `side view`, `front view` and `top view`, respectively. `lh` and `rh` denote `left hand` and `right hand`, respectively. `aa` and `pt` denote `atomic action` and `primitive task`, respectively.

Folder `features` contains the I3D features. Folder `groundTruth` contains the action annoations. Folder `splits` contains the `training.bundle` and `testing.bundle` that tell you the video lists for training and testing.

## Model training and evaluation 
The models and scripts of [MS-TCN](https://github.com/yabufarha/ms-tcn), [DTGRM](https://github.com/redwang/DTGRM), and [BCN](https://github.com/MCG-NJU/BCN) are stored in subfolders `ms-tcn`, `DTGRM`, and `BCN`.

## Checkpoints
We provide the pretrained best checkpoints for each model in the folder `checkpoints`.

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

We appreciate the collaborators/maintainers of the [MS-TCN](https://github.com/yabufarha/ms-tcn), [DTGRM](https://github.com/redwang/DTGRM), and [BCN](https://github.com/MCG-NJU/BCN) repositories.

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License, found here. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.