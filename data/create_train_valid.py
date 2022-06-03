import os
import pdb
import random
import shutil
random.seed(2022)

all_files = os.listdir('images')

for file in all_files:
	if random.random() > 0.8:
		shutil.copyfile('images/'+file, 'valid/'+file)
	else:
		shutil.copyfile('images/'+file, 'train/'+file)