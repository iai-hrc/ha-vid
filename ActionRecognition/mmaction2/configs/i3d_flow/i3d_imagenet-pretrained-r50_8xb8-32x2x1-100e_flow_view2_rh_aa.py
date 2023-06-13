model = dict(
    type='Recognizer3D',
    backbone=dict(
        type='ResNet3d',
        pretrained2d=True,
        pretrained='torchvision://resnet50',
        depth=50,
        conv1_kernel=(5, 7, 7),
        conv1_stride_t=2,
        pool1_stride_t=2,
        conv_cfg=dict(type='Conv3d'),
        norm_eval=False,
        inflate=((1, 1, 1), (1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (0, 1, 0)),
        zero_init_residual=False,
        in_channels=2,
        with_pool2=False),
    cls_head=dict(
        type='I3DHead',
        num_classes=219,
        in_channels=2048,
        spatial_type='avg',
        dropout_ratio=0.5,
        init_std=0.01,
        average_clips='score'),
    data_preprocessor=dict(
        type='ActionDataPreprocessor',
        mean=[128, 128],
        std=[128, 128],
        format_shape='NCTHW'))
train_cfg = dict(
    type='EpochBasedTrainLoop', max_epochs=100, val_begin=1, val_interval=1)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')
param_scheduler = [
    dict(
        type='MultiStepLR',
        begin=0,
        end=100,
        by_epoch=True,
        milestones=[40, 80],
        gamma=0.1)
]
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001),
    clip_grad=dict(max_norm=40, norm_type=2))
default_scope = 'mmaction'
default_hooks = dict(
    runtime_info=dict(type='RuntimeInfoHook'),
    timer=dict(type='IterTimerHook'),
    logger=dict(type='LoggerHook', interval=20, ignore_last=False),
    param_scheduler=dict(type='ParamSchedulerHook'),
    checkpoint=dict(
        type='CheckpointHook', interval=5, save_best='auto', max_keep_ckpts=5),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    sync_buffers=dict(type='SyncBuffersHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
    dist_cfg=dict(backend='nccl'))
log_processor = dict(type='LogProcessor', window_size=20, by_epoch=True)
vis_backends = [dict(type='LocalVisBackend')]
visualizer = dict(
    type='ActionVisualizer', vis_backends=[dict(type='LocalVisBackend')])
log_level = 'INFO'
load_from = None
resume = False
img_norm_cfg = dict(mean=[128, 128], std=[128, 128])
dataset_type = 'RawframeDataset'
data_root = 'data/view2_rh_aa/rawframes_train'
data_root_val = 'data/view2_rh_aa/rawframes_val'
ann_file_train = 'data/view2_rh_aa/view2_rh_aa_train_list_rawframes.txt'
ann_file_val = 'data/view2_rh_aa/view2_rh_aa_val_list_rawframes.txt'
ann_file_test = 'data/view2_rh_aa/view2_rh_aa_val_list_rawframes.txt'
file_client_args = dict(io_backend='disk')
train_pipeline = [
    dict(type='SampleFrames', clip_len=32, frame_interval=2, num_clips=1),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(
        type='MultiScaleCrop',
        input_size=224,
        scales=(1, 0.8),
        random_crop=False,
        max_wh_scale_gap=0),
    dict(type='Resize', scale=(224, 224), keep_ratio=False),
    dict(type='Normalise', mean=[128, 128], std=[128, 128]),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
val_pipeline = [
    dict(
        type='SampleFrames',
        clip_len=32,
        frame_interval=2,
        num_clips=1,
        test_mode=True),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='Normalise', mean=[128, 128], std=[128, 128]),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
test_pipeline = [
    dict(
        type='SampleFrames',
        clip_len=32,
        frame_interval=2,
        num_clips=1,
        test_mode=True),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='Normalise', mean=[128, 128], std=[128, 128]),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
train_dataloader = dict(
    batch_size=4,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type='RawframeDataset',
        ann_file='data/view2_rh_aa/view2_rh_aa_train_list_rawframes.txt',
        data_prefix=dict(img='data/view2_rh_aa/rawframes_train'),
        start_index=0,
        modality='Flow',
        filename_tmpl='flow_{}_{:05d}.jpg',
        pipeline=[
            dict(
                type='SampleFrames',
                clip_len=32,
                frame_interval=2,
                num_clips=1),
            dict(type='RawFrameDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(
                type='MultiScaleCrop',
                input_size=224,
                scales=(1, 0.8),
                random_crop=False,
                max_wh_scale_gap=0),
            dict(type='Resize', scale=(224, 224), keep_ratio=False),
            dict(type='Normalise', mean=[128, 128], std=[128, 128]),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='PackActionInputs')
        ]))
val_dataloader = dict(
    batch_size=4,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='RawframeDataset',
        ann_file='data/view2_rh_aa/view2_rh_aa_val_list_rawframes.txt',
        data_prefix=dict(img='data/view2_rh_aa/rawframes_val'),
        start_index=0,
        modality='Flow',
        filename_tmpl='flow_{}_{:05d}.jpg',
        pipeline=[
            dict(
                type='SampleFrames',
                clip_len=32,
                frame_interval=2,
                num_clips=1,
                test_mode=True),
            dict(type='RawFrameDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(type='CenterCrop', crop_size=224),
            dict(type='Normalise', mean=[128, 128], std=[128, 128]),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='PackActionInputs')
        ],
        test_mode=True))
test_dataloader = dict(
    batch_size=1,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='RawframeDataset',
        ann_file='data/view2_rh_aa/view2_rh_aa_val_list_rawframes.txt',
        data_prefix=dict(img='data/view2_rh_aa/rawframes_val'),
        start_index=0,
        modality='Flow',
        filename_tmpl='flow_{}_{:05d}.jpg',
        pipeline=[
            dict(
                type='SampleFrames',
                clip_len=32,
                frame_interval=2,
                num_clips=1,
                test_mode=True),
            dict(type='RawFrameDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(type='CenterCrop', crop_size=224),
            dict(type='Normalise', mean=[128, 128], std=[128, 128]),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='PackActionInputs')
        ],
        test_mode=True))
val_evaluator = dict(type='AccMetric')
test_evaluator = dict(type='AccMetric')
auto_scale_lr = dict(enable=True, base_batch_size=64)
launcher = 'none'
work_dir = './work_dirs/i3d_imagenet-pretrained-r50_8xb8-32x2x1-100e_flow_view2_rh_aa'
randomness = dict(seed=None, diff_rank_seed=False, deterministic=False)

