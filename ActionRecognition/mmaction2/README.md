# mmaction2 Action Recognition for HA-ViD
This repository contains checkpoints and config files for the Action Recognition I3D, TimeSFormer, and MVITv2 on HA-ViD using [mmaction2](https://github.com/open-mmlab/mmaction2).

## Installation

Installation followed the instructions from the mmaction [installation](https://mmaction2.readthedocs.io/en/latest/get_started/installation.html) documentation.

Dependencies that differ from the documentation are listed below:

1. Python 3.9
2. Cuda 11.7
3. PyTorch 1.13.1
4. Torchvision 0.14.1
5. pytorchvideo (via `pip install pytorchvideo`)


## Training and testing

Training and testing followed the instructions from the mmaction [documentation](https://mmaction2.readthedocs.io/en/latest/index.html).

### Combining views and modality

For MVITv2 combined view and I3D rgb+flow, the features before the softmax layer were obtained (by specifying `average_clips='score'` in the configuration file), then fused using the [report_accuracy.py](https://github.com/open-mmlab/mmaction2/blob/main/tools/analysis_tools/report_accuracy.py) script provided in mmaction2 with coefficients of 1.0.

## Acknowledgement

We appreciate the collaborators/maintainers of [mmaction2](https://github.com/open-mmlab/mmaction2).

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.