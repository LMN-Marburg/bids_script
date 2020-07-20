import os
import sys
import subprocess
import shutil

## delete remaining anat and func logfiles created by Jens, as they are not needed

#get folder where all the data is inside
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
			#look for anat and func measurements and delete respective logfile
			if 'anat' in i and os.path.exists(folder1_path+j+'/anat/_logfile.txt'):
				os.remove(folder1_path+j+'/anat/_logfile.txt')
			elif 'func' in i and os.path.exists(folder1_path+j+'/func/_logfile.txt'):
				os.remove(folder1_path+j+'/func/_logfile.txt')
			else:
				pass

