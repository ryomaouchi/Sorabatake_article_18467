'''
This file is used to create a gif file of generated images.
'''

from glob import glob
from PIL import Image

path_list = ["./data/i" + str(i) + ".png" for i in [1, 5, 10, 15, 20, 30, 40, 50, 75, 100, 200, 300, 400, 500]]

images = list(map(lambda file : Image.open(file) , path_list))
    
images[0].save('out.gif', save_all=True, append_images=images[1:], optimize=False, duration=800, loop=0)
