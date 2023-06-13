model = dict(
    type='Recognizer3D',
    backbone=dict(
        type='MViT',
        arch='small',
        drop_path_rate=0.1,
        dim_mul_in_attention=False,
        pretrained=
        'https://download.openmmlab.com/mmselfsup/1.x/maskfeat/maskfeat_mvit-small_16xb32-amp-coslr-300e_k400/maskfeat_mvit-small_16xb32-amp-coslr-300e_k400_20230131-87d60b6f.pth',
        pretrained_type='maskfeat'),
    data_preprocessor=dict(
        type='ActionDataPreprocessor',
        mean=[114.75, 114.75, 114.75],
        std=[57.375, 57.375, 57.375],
        format_shape='NCTHW',
        blending=dict(
            type='RandomBatchAugment',
            augments=[
                dict(type='MixupBlending', alpha=0.8, num_classes=75),
                dict(type='CutmixBlending', alpha=1, num_classes=75)
            ])),
    cls_head=dict(
        type='MViTHead',
        in_channels=768,
        num_classes=75,
        label_smooth_eps=0.1,
        average_clips='score',
        dropout_ratio=0.0,
        init_scale=0.001))
default_scope = 'mmaction'
default_hooks = dict(
    runtime_info=dict(type='RuntimeInfoHook'),
    timer=dict(type='IterTimerHook'),
    logger=dict(type='LoggerHook', interval=100, ignore_last=False),
    param_scheduler=dict(type='ParamSchedulerHook'),
    checkpoint=dict(
        type='CheckpointHook', interval=3, save_best='auto',
        max_keep_ckpts=20),
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
dataset_type = 'VideoDataset'
data_root = 'data/view0_rh_pt/videos_train'
data_root_val = 'data/view0_rh_pt/videos_val'
ann_file_train = 'data/view0_rh_pt/view0_rh_pt_train_list_videos.txt'
ann_file_val = 'data/view0_rh_pt/view0_rh_pt_val_list_videos.txt'
ann_file_test = 'data/view0_rh_pt/view0_rh_pt_val_list_videos.txt'
file_client_args = dict(io_backend='disk')
train_pipeline = [
    dict(type='DecordInit', io_backend='disk'),
    dict(type='SampleFrames', clip_len=16, frame_interval=4, num_clips=1),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='PytorchVideoWrapper', op='RandAugment', magnitude=7),
    dict(type='RandomResizedCrop'),
    dict(type='Resize', scale=(224, 224), keep_ratio=False),
    dict(type='Flip', flip_ratio=0.5),
    dict(type='RandomErasing', erase_score=0.25, mode='rand'),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
val_pipeline = [
    dict(type='DecordInit', io_backend='disk'),
    dict(
        type='SampleFrames',
        clip_len=16,
        frame_interval=4,
        num_clips=1,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
test_pipeline = [
    dict(type='DecordInit', io_backend='disk'),
    dict(
        type='SampleFrames',
        clip_len=16,
        frame_interval=4,
        num_clips=1,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
repeat_sample = 2
train_dataloader = dict(
    batch_size=4,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='repeat_pseudo_collate'),
    dataset=dict(
        type='RepeatAugDataset',
        num_repeats=2,
        ann_file='data/view0_rh_pt/view0_rh_pt_train_list_videos.txt',
        data_prefix=dict(video='data/view0_rh_pt/videos_train'),
        pipeline=[
            dict(type='DecordInit', io_backend='disk'),
            dict(
                type='SampleFrames',
                clip_len=16,
                frame_interval=4,
                num_clips=1),
            dict(type='DecordDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(type='PytorchVideoWrapper', op='RandAugment', magnitude=7),
            dict(type='RandomResizedCrop'),
            dict(type='Resize', scale=(224, 224), keep_ratio=False),
            dict(type='Flip', flip_ratio=0.5),
            dict(type='RandomErasing', erase_score=0.25, mode='rand'),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='PackActionInputs')
        ]))
val_dataloader = dict(
    batch_size=4,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='VideoDataset',
        ann_file='data/view0_rh_pt/view0_rh_pt_val_list_videos.txt',
        data_prefix=dict(video='data/view0_rh_pt/videos_val'),
        pipeline=[
            dict(type='DecordInit', io_backend='disk'),
            dict(
                type='SampleFrames',
                clip_len=16,
                frame_interval=4,
                num_clips=1,
                test_mode=True),
            dict(type='DecordDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(type='CenterCrop', crop_size=224),
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
        type='VideoDataset',
        ann_file='data/view0_rh_pt/view0_rh_pt_val_list_videos.txt',
        data_prefix=dict(video='data/view0_rh_pt/videos_val'),
        pipeline=[
            dict(type='DecordInit', io_backend='disk'),
            dict(
                type='SampleFrames',
                clip_len=16,
                frame_interval=4,
                num_clips=1,
                test_mode=True),
            dict(type='DecordDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(type='CenterCrop', crop_size=224),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='PackActionInputs')
        ],
        test_mode=True))
val_evaluator = dict(type='AccMetric')
test_evaluator = dict(type='AccMetric')
train_cfg = dict(
    type='EpochBasedTrainLoop', max_epochs=100, val_begin=1, val_interval=1)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')
base_lr = 0.0096
optim_wrapper = dict(
    optimizer=dict(
        type='AdamW', lr=0.0096, betas=(0.9, 0.999), weight_decay=0.05),
    constructor='LearningRateDecayOptimizerConstructor',
    paramwise_cfg=dict(
        decay_rate=0.75, decay_type='layer_wise', num_layers=16),
    clip_grad=dict(max_norm=5, norm_type=2))
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.0016666666666666668,
        by_epoch=True,
        begin=0,
        end=20,
        convert_to_iter_based=True),
    dict(
        type='CosineAnnealingLR',
        T_max=80,
        eta_min_ratio=0.0016666666666666668,
        by_epoch=True,
        begin=20,
        end=100,
        convert_to_iter_based=True)
]
auto_scale_lr = dict(enable=True, base_batch_size=256)
launcher = 'none'
work_dir = './work_dirs/mvit-small-p244_32xb16-16x4x1-200e_view0_rh_pt'
randomness = dict(seed=None, diff_rank_seed=False, deterministic=False)

