#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:20:14 2018

@author: cumtb822
"""

from PIL import Image
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def convert(dir,width,height):
    file_list = os.listdir(dir)
    print(file_list)
    for filename in file_list:
        path=''
        path=dir+filename
        im=Image.open(path)
        out=im.resize((64,64),Image.ANTIALIAS)
        print ("%s has been resized!"%filename)
        out.save(path)
        print("success")
if __name__ == '__main__':
   #dir = raw_input('please input the operate dir:')
   convert("C:\\Users\changjianhui\Desktop\Colorization\Colorization-GAN\colorImage/",64,64)
        