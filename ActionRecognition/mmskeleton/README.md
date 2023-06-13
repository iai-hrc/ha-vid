# mmaction2 Action Recognition for HA-ViD
This repository contains checkpoints and config files for the Action Recognition ST-GCN on HA-ViD using [mmskeleton](https://github.com/open-mmlab/mmskeleton).

## Installation

Installation followed the instructions from the mmskeleton [installation](https://github.com/open-mmlab/mmskeleton/blob/master/doc/GETTING_STARTED.md) documentation.

*Note, to install mmskeleton on Cuda 11, we use the [pull-request](https://github.com/open-mmlab/mmskeleton/pull/416) made by @SebastianLinker.  

Dependencies that differ from the documentation are listed below:

1. Python 3.9
2. Cuda 11.1
3. PyTorch 1.8.1
4. Torchvision 0.9.1
5. mmcv-full 1.3.3 
6. mmdet 2.12.0

## Data
Note, the skeleton data (.pkl) only contain the upper 26 joints of the Azure Kinect skeleton. This is because the lower joints of the participants are hidden behind the workbench. 

## Training and testing

The configuration files for training and testing need to specify the skeleton layout. This is defined in `./mmskeleton/mmskeleton/ops/st_gcn/graph.py`. 
We provide an updated graph.py file which contains the layouts for `azure` and `azure-upper` which define the 32 Azure Kinect skeleton layout and the upper 26 joints of the Azure Kinect skeleton layout respectively.
This file must be replaced to run training and testing on the provided configuration files.

To train the model, run `mmskl [training config] --gpus [GPUs]`

To test the model, run `mmskl [testing config] --gpus [GPUs] --checkpoint [checkpoint]`

## Acknowledgement

We appreciate the collaborators/maintainers of [mmskeleton](https://github.com/open-mmlab/mmskeleton).

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.