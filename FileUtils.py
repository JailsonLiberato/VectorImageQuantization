#coding: utf-8
from PIL import Image
from numpy import array
from PGMFile import PGMFileClass

class FileUtilsClass:
    def pgmread(self, filename):
       img = Image.open(filename)
       return array(img)

    def pgmwrite(self, arr):
       img = Image.fromarray(arr)
       img.save("output.pgm")
       img.close()