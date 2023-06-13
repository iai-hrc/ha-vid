import torch
from model import Trainer
from batch_gen import BatchGenerator
import os
import argparse
import random

import time

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
seed = 1538574472
random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
torch.backends.cudnn.deterministic = True

parser = argparse.ArgumentParser()
parser.add_argument('--action', default='train')
parser.add_argument('--dataset', default="assembly_view0_lh_aa")
parser.add_argument('--split', default='1')
parser.add_argument('--num_stages', type=str, default='4')
parser.add_argument('--num_layers', type=str, default='10')
parser.add_argument('--num_f_maps', type=str, default='64')
parser.add_argument('--df_size', type=str, default='3')

args = parser.parse_args()

num_stages = int(args.num_stages)
num_layers = int(args.num_layers)
num_f_maps = int(args.num_f_maps)
df_size = int(args.df_size)

features_dim = 2048
bz = 10
lr = 0.0005
num_epochs = 1000
sample_rate = 1

vid_list_file = "../data/"+args.dataset+"/splits/train.split"+args.split+".bundle"
vid_list_file_tst = "../data/"+args.dataset+"/splits/test.split"+args.split+".bundle"
features_path = "../data/features/"
gt_path = "../data/"+args.dataset+"/groundTruth/"

mapping_file = "../data/"+args.dataset+"/mapping.txt"

model_dir = "./models/"+args.dataset+"/split_"+args.split+"/stages_"+\
args.num_stages+"_layers_"+args.num_layers+"_fmaps_"+args.num_f_maps+"_dfsize_"+args.df_size
results_dir = "./results/"+args.dataset+"/split_"+args.split+"/stages_"+\
args.num_stages+"_layers_"+args.num_layers+"_fmaps_"+args.num_f_maps+"_dfsize_"+args.df_size
 
if not os.path.exists(model_dir):
    os.makedirs(model_dir)
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

file_ptr = open(mapping_file, 'r')
actions = file_ptr.read().split('\n')[:-1]
file_ptr.close()
actions_dict = dict()
for a in actions:
    actions_dict[a.split()[1]] = int(a.split()[0])

num_classes = len(actions_dict)

trainer = Trainer(num_stages, num_layers, num_f_maps, features_dim, num_classes)
if args.action == "train":
    start_time = time.perf_counter()
    training_time = open(model_dir+'/training_time.txt','w')
    print("Train::"+args.dataset+"_split_"+args.split+"---stages_"+args.num_stages+
        "_layers_"+args.num_layers+"_fmaps_"+args.num_f_maps+"_dfsize_"+args.df_size)
    batch_gen = BatchGenerator(num_classes, actions_dict, gt_path, features_path, sample_rate)
    batch_gen.read_data(vid_list_file)
    trainer.train(model_dir, batch_gen, num_epochs=num_epochs, batch_size=bz, learning_rate=lr, device=device)
    end_time = time.perf_counter()
    training_time.write('total training time: {}'.format(round(end_time-start_time)))

if args.action == "predict":
    test_acc_list = open(model_dir+'/training_reault.txt','r')
    lines = test_acc_list.readlines()
    for line in lines:
        accs = [line[-10:-1] for line in lines]
    test_epochs = accs.index(max(accs))+1
    best_epoch = open(model_dir+'/best_epoch.txt','w')
    best_epoch.write(str(test_epochs))
    best_epoch.close()
    print("Predict::"+args.dataset+"_split_"+args.split+"---stages_"+args.num_stages+
        "_layers_"+args.num_layers+"_fmaps_"+args.num_f_maps+"_dfsize_"+args.df_size)
    trainer.predict(model_dir, results_dir, features_path, vid_list_file_tst, test_epochs, 
        actions_dict, device, sample_rate)
