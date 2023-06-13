# TSM Action Recognition for HA-ViD
This repository contains checkpoints and config files for the Action Recognition TSM on HA-ViD using [temporal-shift-module](https://github.com/mit-han-lab/temporal-shift-module).

## Installation

Installation followed the instructions from the temporal-shift-module [prerequisites](https://github.com/open-mmlab/mmskeleton/blob/master/doc/GETTING_STARTED.md).

Minor changes need to made after installing the dependencies and cloning the git repository.
* Instead of separate configuration files for each hand, view, annotation type, all the configurations are setup in  `./ops/dataset_config.py`. Therefore, this file must be replaced with the `dataset_config.py` file we provide, which has added the configurations required for HA-ViD. Note, you will still need to update the `ROOT_DATASET` path to match your data directory.
* Additionally, line 39 in `./ops/utils.py` causes an error on pytorch 1.7.1. Therefore, following the [suggestion](https://github.com/pytorch/examples/issues/836) from @seemethere, replace `view` with `reshape`


## Training and testing

The configuration files for training and testing need to specify the skeleton layout. This is defined in `./mmskeleton/mmskeleton/ops/st_gcn/graph.py`. 
We provide an updated graph.py file which contains the layouts for `azure` and `azure-upper` which define the 32 Azure Kinect skeleton layout and the upper 26 joints of the Azure Kinect skeleton layout respectively.
This file must be replaced to run training and testing on the provided configuration files.

To train the model, run `python main.py [dataset] RGB --arch resnet50 --num_segments 8 --gd 20 --lr 0.0025 --wd 1e-4 --lr_steps 20 40 --epochs 50 --batch-size 16 -j 16 --dropout 0.5 --consensus_type=avg --eval-freq=1 --shift --shift_div=8 --shift_place=blockres --npb`

## Acknowledgement

We appreciate the collaborators/maintainers of [temporal-shift-module](https://github.com/mit-han-lab/temporal-shift-module).

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License, found here. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.