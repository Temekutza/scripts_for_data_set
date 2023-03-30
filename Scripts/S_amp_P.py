from sys import argv
import os
import skimage
from skimage import io
import numpy as np

#script_path = os.getcwd()
files_path = argv[1]
#file_name = argv[2]
os.chdir(files_path)

def add_noise(img, coeff, name):
    for s in coeff:
        temp = skimage.util.random_noise(img,mode="s&p",seed=None, clip=True, amount = s)
        io.imsave(name + '_noise' + str(s).replace('.', '') + '.jpg', temp)

## run indefinitely
## get the directory listing
jpegfiles = [name for name in os.listdir('.')
    if name.endswith('.jpg')]
## save img
for art in jpegfiles:
    img = io.imread (art)
    img = np.array (img)
    name, ext = art.split('.')
    add_noise(img, [0.2, 0.15, 0.25], name)