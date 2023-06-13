# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu

import os

ROOT_DATASET = './data'


def return_kinetics(modality):
    filename_categories = 400
    if modality == 'RGB':
        root_data = ROOT_DATASET + 'kinetics/images'
        filename_imglist_train = 'kinetics/labels/train_videofolder.txt'
        filename_imglist_val = 'kinetics/labels/val_videofolder.txt'
        prefix = 'img_{:05d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix

def return_assembly(modality,dataset):
    if 'pt' in dataset:
        filename_categories = 75
    elif 'aa' in dataset:
        filename_categories = 219
    if modality == 'RGB':
        root_data = ROOT_DATASET + dataset
        filename_imglist_train = dataset + '/' + dataset + '_tsm_train_list.txt'
        filename_imglist_val = dataset + '/' + dataset + '_tsm_val_list.txt'
        prefix = 'img_{:05d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix

def return_dataset(dataset, modality):
    dict_single = {'view0_lh_aa':return_assembly, 'view0_lh_pt':return_assembly, 'view0_rh_pa':return_assembly, 'view0_lh_pt':return_assembly, 
                   'view1_lh_aa':return_assembly, 'view1_lh_pt':return_assembly, 'view1_rh_pa':return_assembly, 'view1_lh_pt':return_assembly,  
                   'view2_lh_aa':return_assembly, 'view2_lh_pt':return_assembly, 'view2_rh_pa':return_assembly, 'view2_lh_pt':return_assembly}

    if dataset in dict_single:
        file_categories, file_imglist_train, file_imglist_val, root_data, prefix = dict_single[dataset](modality,dataset)
    else:
        raise ValueError('Unknown dataset '+dataset)

    file_imglist_train = os.path.join(ROOT_DATASET, file_imglist_train)
    file_imglist_val = os.path.join(ROOT_DATASET, file_imglist_val)
    if isinstance(file_categories, str):
        file_categories = os.path.join(ROOT_DATASET, file_categories)
        with open(file_categories) as f:
            lines = f.readlines()
        categories = [item.rstrip() for item in lines]
    else:  # number of categories
        categories = [None] * file_categories
    n_class = len(categories)
    print('{}: {} classes'.format(dataset, n_class))
    return n_class, file_imglist_train, file_imglist_val, root_data, prefix
