import os
import json
import argparse


def find_name(image_id, test_data):
    for item in test_data['images']:
        if item['id'] == image_id:
            return item['file_name']
    return -1

def get_tracking_gt(file,output):
    data = json.load(file)
    data_writer = open(output,'w')
    for annotation in data["annotations"]:
        image_id = annotation["image_id"]
        image_name = find_name(image_id, data)
        frame_id = int(str.split(image_name,'.')[0].split('_')[-1])
        track_id = annotation["attributes"]["track_id"] #start from 0
        track_id = int(track_id) + 1
        bbox = annotation["bbox"]
        bbox_1 = bbox[0]
        bbox_2 = bbox[1]
        bbox_3 = bbox[2]
        bbox_4 = bbox[3]
        conf = 1
        x = -1
        y = -1
        x = -1
        data_writer.write(str(frame_id) + ',' + str(track_id) + ',' + str(bbox_1) + ',' + str(bbox_2) + ',' + str(bbox_3) + ',' + str(bbox_4) 
                          + ',' + str(conf) + ',' + str(x) + ',' + str(y) + ',' + str(x) +'\n')
    data_writer.close()
    return -1

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default="./S19A05I01S1/annotations/annotation.json", help = 'path to the annotation file', required=True)
    args = parser.parse_args()
    video_name = args.f.split('/')[-3]
    if not os.path.exists('./outputs/'+video_name):
        os.makedirs('./outputs/'+video_name)
    output = './outputs/'+ video_name +'/tracking_gt.txt'

    file = open(args.f)
    gt = get_tracking_gt(file,output)

    print('{} is generated'.format(output))

