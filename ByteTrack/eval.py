import motmetrics as mm
import argparse
import numpy as np 
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-gt', default="./outputs/s19a05i01s1/tracking_gt.txt", help='path to the tracking gt file', required=True)
    parser.add_argument('-tr', default="./outputs/s19a05i01s1/tracklets.txt", help='path to the tracking result file', required=True)
    args = parser.parse_args()
    video_name = args.gt.split('/')[-2]
    
    output_path = './outputs/'+video_name
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = open('./outputs/'+video_name+'/eval_results.txt','w')
    

    metrics = list(mm.metrics.motchallenge_metrics)

    gt=mm.io.loadtxt(args.gt, fmt="mot15-2D", min_confidence=1)
    tr=mm.io.loadtxt(args.tr, fmt="mot15-2D")
    name=os.path.splitext(os.path.basename(args.tr))[0]

    acc=mm.utils.compare_to_groundtruth(gt, tr, 'iou', distth=0.5)
    mh = mm.metrics.create()
    summary = mh.compute(acc, metrics=metrics, name=name)
    output_file.write(mm.io.render_summary(summary, formatters=mh.formatters,namemap=mm.io.motchallenge_metric_names))

    print(mm.io.render_summary(summary, formatters=mh.formatters,namemap=mm.io.motchallenge_metric_names))
