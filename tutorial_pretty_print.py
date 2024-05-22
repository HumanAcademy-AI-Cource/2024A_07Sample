#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import pprint

def detect_labels_local_file(photo):


    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)    
    pprint.pprint(response, sort_dicts=False) # pprintで表示する処理に置き換え

    return len(response['Labels'])

def main():
    photo='images/001.png' # 変更した場所

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
