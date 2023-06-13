import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default="./outputs/S19A04I01M0/tracking_gt.txt", help='path to the tracking_gt.txt file', required=True)
    args = parser.parse_args()
    video_name = args.f.split('/')[-2]
    if not os.path.exists('./outputs/'+video_name):
        os.makedirs('./outputs/'+video_name)

    output_path = './outputs/' + video_name + '/dets_gt.txt'

    input_file = open(args.f,'r')
    input_read = input_file.readlines()
    output_file = open(output_path,'w')

    for line in input_read:
        frame_id = str(line.split(',')[0].zfill(6))
        output_file.write(frame_id + ',' + '-1' + ',' + str(line.split(',')[2]) + ',' + str(line.split(',')[3])
                          + ',' + str(line.split(',')[4]) + ','
                          + str(line.split(',')[5])+'\n')
    
