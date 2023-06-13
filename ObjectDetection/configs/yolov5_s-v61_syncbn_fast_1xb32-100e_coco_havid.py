_base_ = '../yolov5/yolov5_s-v61_syncbn_fast_8xb16-300e_coco.py'

max_epochs = 50  # maximum epochs for training
data_root = '../data'  # the path to data folder

# the path of result save, can be omitted, omitted save file name is located under work_dirs with the same name of config file.
# If a config variable changes only part of its parameters, changing this variable will save the new training file elsewhere
work_dir = './work_dirs/yolov5_s-v61_syncbn_fast_1xb32-100e_coco_havid'

# load_from can specify a local path or URL, setting the URL will automatically download, because the above has been downloaded, we set the local path here
# since this tutorial is fine-tuning on the cat dataset, we need to use `load_from` to load the pre-trained model from MMYOLO. This allows for faster convergence and accuracy
load_from = 'the path to pretrained checkpoint file'

# according to your GPU situation, modify the batch size, and YOLOv5-s defaults to 8 cards x 16bs
train_batch_size_per_gpu = 32
train_num_workers = 4  # recommend to use train_num_workers = nGPU x 4

save_epoch_intervals = 2  # save weights every interval round

# according to your GPU situation, modify the base_lr, modification ratio is base_lr_default * (your_bs / default_bs)
base_lr = _base_.base_lr / 4

anchors = [  # the anchor has been updated according to the characteristics of dataset. The generation of anchor will be explained in the following section.
    [(68, 69), (154, 91), (143, 162)],  # P3/8
    [(242, 160), (189, 287), (391, 207)],  # P4/16
    [(353, 337), (539, 341), (443, 432)]  # P5/32
]

class_name = ("Ball", "Ball Seat","Box","Cylinder Base","Cylinder Cap","Cylinder Bracket","Cylinder Subassembly","Shaft","Gear Large","Gear Small","Worm Gear","Hand-dial","Quarter-turn Handle","Hand-wheel","Bar","Rod","Linear Bearing","Nut","Spacer Large","Spacer Small","Screw (hex)","Screw (philips)","USB Male","Hole C1","Hole C2","Hole C3","Hole C4","Hole G1 (GL)","Hole G2 (GS)","Hole G3 (GW)","Hole N1 (NR)","Hole N2 (NB)","Hole N3 (NL)","Hole N4 (NS)","Hole/Stud N5 (NN)","Hole N6 (NU)","Screwdriver (hex)","Screwdriver (philips)","Wrench (nut)","Wrench (shaft)","Hand","Bolt")# according to the label information of class_with_id.txt, set the class_name
num_classes = len(class_name)
metainfo = dict(
    classes=class_name,
)

train_cfg = dict(
    max_epochs=max_epochs,
    val_begin=20,  # number of epochs to start validation.  Here 20 is set because the accuracy of the first 20 epochs is not high and the test is not meaningful, so it is skipped
    val_interval=save_epoch_intervals  # the test evaluation is performed  iteratively every val_interval round
)

model = dict(
    bbox_head=dict(
        head_module=dict(num_classes=num_classes),
        prior_generator=dict(base_sizes=anchors),

        # loss_cls is dynamically adjusted based on num_classes, but when num_classes = 1, loss_cls is always 0
        loss_cls=dict(loss_weight=0.5 *
                      (num_classes / 80 * 3 / _base_.num_det_layers))))

train_dataloader = dict(
    batch_size=train_batch_size_per_gpu,
    num_workers=train_num_workers,
    dataset=dict(
        _delete_=True,
        type='RepeatDataset',#'CocoDataset',
        # if the dataset is too small, you can use RepeatDataset, which repeats the current dataset n times per epoch, where 5 is set.
        times=1,
        dataset=dict(
            type=_base_.dataset_type,
            data_root=data_root,
            metainfo=metainfo,
            ann_file='train/annotations/annotation.json',
            data_prefix=dict(img='train/images/'),
            filter_cfg=dict(filter_empty_gt=False, min_size=32),
            pipeline=_base_.train_pipeline)))

val_dataloader = dict(
    dataset=dict(
        metainfo=metainfo,
        data_root=data_root,
        ann_file='val/annotations/annotation.json',
        data_prefix=dict(img='val/images/')))

test_dataloader = val_dataloader

val_evaluator = dict(ann_file=data_root + 'val/annotations/annotation.json')
test_evaluator = val_evaluator

optim_wrapper = dict(optimizer=dict(lr=base_lr))

default_hooks = dict(
    # set how many epochs to save the model, and the maximum number of models to save,`save_best` is also the best model (recommended).
    checkpoint=dict(
        type='CheckpointHook',
        interval=save_epoch_intervals,
        max_keep_ckpts=5,
        save_best='auto'),
    param_scheduler=dict(max_epochs=max_epochs),
    # logger output interval
    logger=dict(type='LoggerHook', interval=10))
