# Run visualization for tracklets of each video sample
#
# Fatemeh Saleh <fatemehsadat.saleh@anu.edu.au>

import cv2
import glob
import random
import argparse
import os


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', default='./outputs_detectedoutput/S19A05I01S1/tracklets.txt',help='path to the tracking result file', required=True)
    parser.add_argument('-root', default='./S19A05I01S1/images', help='path to the images file', required=True)
    args = parser.parse_args()

    input = args.s

    fid = open(input, 'r')
    lines = fid.read()
    lines = str.split(lines, '\n')[0:-1]

    if not os.path.exists('./outputs/tracking_results'):
        os.mkdir('./outputs/tracking_results')

    frames = glob.glob(args.root + '/*')
    frames.sort()
    frames_dic = {}
    exist_ids = {}

    for line in lines:
        items = str.split(line, ',')
        id = int(items[1])
        x = float(items[2])
        y = float(items[3])
        w = float(items[4])
        h = float(items[5])
        frame = int(items[0])
        if frame not in frames_dic:
            frames_dic[frame] = []
        frames_dic[frame].append([x, y, w, h, id])

    for key, value in frames_dic.items():
        I = cv2.imread(frames[key])
        for v in value:
            if v[-1] not in exist_ids.keys():
                r = lambda: random.randint(0, 255)
                exist_ids[v[-1]] = (r(), r(), r())
                cv2.rectangle(I, (int(v[0]), int(v[1])), (int(v[0] + v[2]), int(v[1] + v[3])), exist_ids[v[-1]], 2)
                cv2.putText(I, str(v[-1]), (int(v[0]) + 10, int(v[1]) + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
            else:
                cv2.rectangle(I, (int(v[0]), int(v[1])), (int(v[0] + v[2]), int(v[1] + v[3])), exist_ids[v[-1]], 2)
                cv2.putText(I, str(v[-1]), (int(v[0]) + 10, int(v[1]) + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

        cv2.imwrite('./outputs/tracking_results'+ '/' + str.split(frames[key], '/')[-1], I)
        print('frame ', key, ' has been written!')
