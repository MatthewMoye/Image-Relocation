import os
import numpy as np
import shutil
from PIL import Image

def move_images(originalDirectory,endDirectory,width,height):
    os.chdir(originalDirectory)
    for file in os.listdir():
        try:
            img = Image.open(file)
            x = np.array(img)
            if(x.shape[0]<=height and x.shape[1]<=width):
                shutil.move(originalDirectory+'/'+file,endDirectory)
        except:
            print('')
