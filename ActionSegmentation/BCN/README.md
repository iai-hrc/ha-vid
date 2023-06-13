# BCN Action Segmentation baseline for HA-ViD.
This repository has been adapted from the original [BCN](https://github.com/MCG-NJU/BCN) repository to train and evaluate on the HA-ViD dataset.


## Dependencies

1. Python 3.7
2. PyTorch 1.8.0
3. Cuda 11.1
4. tensorboard and tensorboardX

## 1. Training full-resolution barrier generation module
* The pretrained model of full BGM is the initialization of BGM in joint-training. In [BCN](https://github.com/MCG-NJU/BCN), only full-resolution BGM can work for joint-training.
* To train the model run `python bgm.py --action train --dataset [dataset] --resolution full` where [dataset] is one of `view0_lh_pt`, `view0_lh_aa`, `view0_rh_pt`, `view0_rh_aa`, `view1_lh_pt`, `view1_lh_aa`, `view1_rh_pt`, `view1_rh_aa`,`view2_lh_pt`, `view2_lh_aa`, `view2_rh_pt`, `view2_rh_aa`.

## 2. Training resized-resolution barrier generation module
* The predicted boundary by pre-trained model of resized BGM is for post-processing. In [BCN](https://github.com/MCG-NJU/BCN) paper, the quality of boundary predicted by resized BGM is slightly better than full BGM.
* To train the model run `python bgm.py --action train --dataset [dataset] --resolution resized` 

## 3. Testing resized-resolution barrier generation module
* The predicted barriers (selected from boundary confidence scores) is saved in .csv file in folder `bgm_result`. 
* To train the model run `python bgm.py --action test --dataset [dataset] --resolution resized`

## 4. Training Stage Cascade Network and BGM jointly
* the parameters of BGM are freezed for the first several epochs and then jointly optimize two modules until convergence. 
* To train the model run `python main.py --action train --dataset [dataset] --resolution resized`

## 5. Testing BCN
* We directly provide the evaluation result of our final result after running
* To test the model run `python main.py --action train --dataset [dataset] --resolution resized`
* The final performance is made by the combination of Stage Cascade, 1 full-LBP and several times of resized-LBP as post-processing.
* The segmenation results are saved in folder `results`

## 6. Evaluation
* You can evaluate the performance of the result predicted in step 5.
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
We appreciate the collaborators/maintainers of the [BCN](https://github.com/MCG-NJU/BCN) repository.

## License
HA-ViD is licensed by us under the Creative Commons Attribution-NonCommerial 4.0 International License. The terms are :
* Attribution : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* NonCommercial : You may not use the material for commercial purposes.