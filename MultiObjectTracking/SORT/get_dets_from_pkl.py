# Convert detections of json format to standard tracking format
#
# Fatemeh Saleh <fatemehsadat.saleh@anu.edu.au>

import pickle
import argparse
import os


# Find image name from image_id
def find_name(image_id, test_data):
    for item in test_data['images']:
        if item['id'] == image_id:
            return item['file_name']
    return -1


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default="./S19A05I01S1/detections/detection_result.pkl", help='path to the detection results', required=True)
    args = parser.parse_args()
    video_name = args.f.split('/')[-3]
    if not os.path.exists('./outputs/'+video_name):
        os.makedirs('./outputs/'+video_name)

    output = './outputs/' + video_name + '/dets.txt'

    input = args.f

    # Select high confident predictions of the model to track
    score_thresh = 0.9
    fid = open(output, 'w')

    test_results = pickle.load(open(input, 'rb'))
    all_boxes_dict = {}
    
    for item in test_results:
        image_path = item["img_path"]
        frame_id = image_path.split('/')[-1].split('.')[0].split('_')[-1]
        bboxes = item["pred_instances"]["bboxes"].tolist()
        scores = item["pred_instances"]["scores"].tolist()
        for i in range(len(bboxes)):
            if scores[i] > score_thresh:
                fid.write(frame_id + ',' + '-1' + ',' + str(bboxes[i][0]) + ',' + str(bboxes[i][1])
                          + ',' + str(bboxes[i][2] - bboxes[i][0]) + ','
                          + str(bboxes[i][3] - bboxes[i][1])+'\n')
    print(output + ' file created for tracking!')        
