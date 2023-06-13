from loguru import logger
import argparse
import numpy as np

#import sys
#sys.path.insert(0, '/home/researchalgorithm/hzhe951/ObjectTracking/ByteTrack')

from model.byte_tracker import BYTETracker
import os
import time


def write_results(filename, results):
    save_format = '{frame},{id},{x1},{y1},{w},{h},{s},-1,-1,-1\n'
    with open(filename, 'w') as f:
        for frame_id, tlwhs, track_ids, scores in results:
            for tlwh, track_id, score in zip(tlwhs, track_ids, scores):
                if track_id < 0:
                    continue
                x1, y1, w, h = tlwh
                line = save_format.format(frame=frame_id, id=track_id, x1=round(x1, 1), y1=round(y1, 1), w=round(w, 1), h=round(h, 1), s=round(score, 2))
                f.write(line)
    logger.info('save results to {}'.format(filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default="./outputs/S04A04I01M0/detections/dets.txt", help='path to the converted detection file', required=True)
    parser.add_argument('-track_thresh', default=0.5)
    parser.add_argument('-track_buffer', default=30)
    parser.add_argument('-mot20', default=False)
    parser.add_argument('-match_thresh', default=0.9)

    args = parser.parse_args()
    video_name = args.f.split('/')[-3]
    if not os.path.exists('outputs/'+video_name):
        os.makedirs('outputs/'+video_name)

    input = args.f
    output = 'outputs/'+video_name + '/tracklets.txt'
    
    ##initializing Tracker
    tracker = BYTETracker(args)
    results = []

    seq_dets = np.loadtxt(input, delimiter=',')  # load detections


    start = time.time()
    for frame in range(int(seq_dets[:, 0].max())+1):
        dets = seq_dets[seq_dets[:, 0] == frame, 2:7]

        trackers = tracker.update(dets)

        online_targets = tracker.update(dets)
        online_tlwhs = []
        online_ids = []
        online_scores = []
        for t in online_targets:
            tlwh = t.tlwh
            tid = t.track_id
            online_tlwhs.append(tlwh)
            online_ids.append(tid)
            online_scores.append(t.score)

        results.append((frame, online_tlwhs, online_ids, online_scores))

    write_results(output, results)
    print('Tracking for ', int(seq_dets[:, 0].max())+1, ' frames Done in ', time.time() - start, ' seconds')
