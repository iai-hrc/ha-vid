_base_ = '../faster_rcnn/faster-rcnn_r101_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=42)),
    init_cfg=dict(type='Pretrained',checkpoint='the path to pretrained checkpoint file'))

data_root = '../data' # the path to data folder
metainfo = {
    'classes': ("Ball", "Ball Seat","Box","Cylinder Base","Cylinder Cap","Cylinder Bracket","Cylinder Subassembly","Shaft","Gear Large","Gear Small","Worm Gear","Hand-dial","Quarter-turn Handle","Hand-wheel","Bar","Rod","Linear Bearing","Nut","Spacer Large","Spacer Small","Screw (hex)","Screw (philips)","USB Male","Hole C1","Hole C2","Hole C3","Hole C4","Hole G1 (GL)","Hole G2 (GS)","Hole G3 (GW)","Hole N1 (NR)","Hole N2 (NB)","Hole N3 (NL)","Hole N4 (NS)","Hole/Stud N5 (NN)","Hole N6 (NU)","Screwdriver (hex)","Screwdriver (philips)","Wrench (nut)","Wrench (shaft)","Hand","Bolt"),
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file= 'train/annotations/annotation.json',
        data_prefix=dict(img='train/images/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='val/annotations/annotation.json', 
        data_prefix=dict(img='val/images/')))
test_dataloader = val_dataloader

val_evaluator = dict(ann_file=data_root + 'val/annotations/annotation.json')
test_evaluator = val_evaluator
