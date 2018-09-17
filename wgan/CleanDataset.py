import cv2
import os
import shutil
from glob import glob
from scipy import misc
import matplotlib.pyplot as plt

#No use
# def isGray(img):
#     if img.ndim == 3:
#         return False
#     else:
#         return True


if __name__ == '__main__':
    data = glob(os.path.join("./data/", "colorImage/", "*.JPEG"))
    print(len(data))
    image_file = data[:len(data)]
    counter = 0
    for one_image in image_file:
        img = misc.imread(one_image)
        if len(img.shape) < 3:
            print(img.shape)
            counter += 1
            os.remove(one_image)
            print("delete %d",counter)
    print(counter)
    print(len(data))
