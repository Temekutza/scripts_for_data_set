import cv2
import os
from sys import argv
from shutil import copyfile 

files_path = argv[1]
os.chdir(files_path)

for name in os.listdir('.'):
    if name.endswith('.jpg'):
    	img = cv2.imread(name)
    	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    	newname,ext = name.split(".")
    	cv2.imwrite(newname+"_gray.jpg", gray)
    	if (newname+".txt") in os.listdir("."):
    		copyfile(newname+".txt",newname+"_gray.txt")
