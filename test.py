import cv2
import numpy as np
import os
import shutil

def a_c(input_file1, input_file2, output_file):
    img1 = cv2.imread(input_file1)
    img2 = cv2.imread(input_file2)
    print(input_file1)
    print(type(img1))
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)
    img = (img1+img2)/2
    img = img.astype(np.uint8)
    print("------------- " + output_file)
    cv2.imwrite(output_file, img)


in_path = './output1'
out_path = './output2'

index = 1
list = os.listdir(in_path)
len = len(os.listdir(in_path))
for file in sorted(os.listdir(in_path)):

    in_path = './output1'
    out_path = './output2'

    if index == 1:
        img_path1 = os.path.join(in_path, file)
        img_path2 = os.path.join(out_path, file)
        shutil.copyfile(img_path1, img_path2)

    print(len-1)
    if index > 1 and index < len:
        img_path1 = os.path.join(in_path, ('%05d' % (index-1)) + '.jpg')
        img_path2 = os.path.join(in_path, file)
        out_path = os.path.join(out_path, file)
        a_c(img_path1, img_path2, out_path)
    elif index >= len:
        break
    index = index + 1



