''''
This file is intended to create the directories used for oil classification.
'''

import os
import random
import shutil
from glob import glob

N = 400 # The number of validation and test data.

random.seed(0)

os.makedirs('Data/training/oil/', exist_ok=True)
os.makedirs('Data/training/no_oil/', exist_ok=True)
#os.makedirs('Data/train/oil_add_generated_images/', exist_ok=True)

os.makedirs('Data/validation/oil/', exist_ok=True)
os.makedirs('Data/validation/no_oil/', exist_ok=True)

os.makedirs('Data/test/oil/', exist_ok=True)
os.makedirs('Data/test/no_oil/', exist_ok=True)

############## 

files = glob("./Data_oil_tank/data/*")

val_files = random.sample(files, N)
for path in val_files:
    shutil.copy(path, 'Data/validation/oil/')

files = list(set(files) - set(val_files))
test_files = random.sample(files, N)
for path in test_files:
    shutil.copy(path, 'Data/test/oil/')

files = list(set(files) - set(test_files))
for path in files:
    shutil.copy(path, 'Data/training/oil/')
    
##############

files =	glob("./Data_no_oil_tank/data/*")

val_files = random.sample(files, N)
for path in val_files:
    shutil.copy(path, 'Data/validation/no_oil/')

files = list(set(files) - set(val_files))
test_files = random.sample(files, N)
for path in test_files:
    shutil.copy(path, 'Data/test/no_oil/')

files = list(set(files) - set(test_files))
for path in files:
    shutil.copy(path, 'Data/training/no_oil/')

##############

#shutil.copytree('Data/train/oil', 'Data/train/oil_add_generated_images')

#files = glob("./Generated_images/*")

do_add_gen = True

if do_add_gen:
    files = []
    for i in range(101,501):
        for j in range(0, 48):
            files.append("Generated_images/gen_" + str(i) +  "_" + str(j) + ".png")

    gen_files = random.sample(files, 2000)
    for path in gen_files:
        shutil.copy(path, 'Data/training/oil/')

##############

print("The size of Data/training/oil is: ", len(glob('Data/training/oil/*')))
print("The size of Data/training/no_oil is: ",len(glob('Data/training/no_oil/*')))
#print("The size of Data/train/oil_add_generated_images is: ",len(glob('Data/train/oil_add_generated_images/*')))

print("The size of Data/validation/oil is: ",len(glob('Data/validation/oil/*')))
print("The size of Data/validation/no_oil is: ",len(glob('Data/validation/no_oil/*')))

print("The size of Data/test/oil is: ",len(glob('Data/test/oil/*')))
print("The size of Data/test/no_oil is: ",len(glob('Data/test/no_oil/*')))
