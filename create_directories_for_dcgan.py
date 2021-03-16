'''
This file is intended to create the directories used for image generation using DCGAN.
'''


import os
import json
from PIL import Image

os.makedirs('Data_oil_tank/data/', exist_ok=True)
os.makedirs('Data_no_oil_tank/data/', exist_ok=True)

json_open = open('labels.json', 'r')
json_load = json.load(json_open)

for v in json_load:
    file_name = './image_patches/'+ v['file_name']
    img = Image.open(file_name)
    if v['label']!='Skip':
        img.save("./Data_oil_tank/data/" + v['file_name'], "JPEG")
    else:
        img.save("./Data_no_oil_tank/data/" + v['file_name'], "JPEG")

print("The size of Data_oil_tank is: ", len(glob("./Data_oil_tank/data/*")))
print("The size of Data_no_oil_tank is: ", len(glob("./Data_no_oil_tank/data/*")))
