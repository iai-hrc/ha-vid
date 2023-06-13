# MS-TCN Action Segmentation baseline for HA-ViD.
This repository has been adapted from the original [MS-TCN](https://github.com/yabufarha/ms-tcn) repository to train and evaluate on the HA-ViD dataset.


## Dependencies
1. Python 3.6
2. PyTorch 1.9.0
3. Cuda 11.1

## 1. Training
* To train the model run `python main.py --action=train --dataset=[dataset]` where [dataset] is one of `view0_lh_pt`, `view0_lh_aa`, `view0_rh_pt`, `view0_rh_aa`, `view1_lh_pt`, `view1_lh_aa`, `view1_rh_pt`, `view1_rh_aa`,`view2_lh_pt`, `view2_lh_aa`, `view2_rh_pt`, `view2_rh_aa`.

## 2. Testing
* To test the model run `python main.py --action=predict --dataset=[dataset]`.
* The segmenation results are saved in folder `results`

## 3. Evaluation
* To evaluate the result run `python eval.py --dataset=[dataset]`.


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

We appreciate the collaborators/maintainers of the [MS-TCN](https://github.com/yabufarha/ms-tcn) repository.
