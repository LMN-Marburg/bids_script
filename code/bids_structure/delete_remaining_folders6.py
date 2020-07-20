import os
import sys
import subprocess
import shutil

## delete remaining folders that are neither anat, func nor fmap

#get folder where all the Data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

#all the sessions
folder1 = os.listdir(folder1_path)

#rename
for j in folder1:
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):	
		#list all sequences 
		folder_in = os.listdir(folder1_path+j)
		for i in folder_in:
			#look for the following measurements and remove others
			if 'anat' in i:
				pass
			elif 'func' in i:
				pass
			elif 'fmap' in i:
				pass
			else:
				if os.path.isdir(folder1_path+j+'/'+i):
					shutil.rmtree(folder1_path+j+'/'+i+'/')

