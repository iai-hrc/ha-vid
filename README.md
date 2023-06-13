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
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.

## Code of Conduct
Code of Conduct of HA-ViD can be found in [Our Website](https://iai-hrc.github.io/ha-vid).