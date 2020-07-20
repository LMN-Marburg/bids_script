import os
import shutil
import sys
import subprocess

## copy and rename the mandatory event-tsv template into the individual func folder

#get folder where all the Data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

#all the sessions
folder1 = os.listdir(folder1_path)

#rename --> kann man noch effizienter gestalten (nur neue abarbeiten)
for j in folder1:
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):	
		#list all sequences 
		folder_in = os.listdir(folder1_path+j)
		#for every sequence	
		for i in folder_in:
			#look for func folder and copy+rename event template
			if i.find('func') > -1:
				if os.path.exists(folder1_path+j+'/'+i+'/'+j+'_task-stuhr_events.tsv'):
					pass
				shutil.copy('/imaging/_data/face_lateralisation_LMN/StUHR_face/scripts/Datenset_2/bids_structure/templates/sub-XXX_task-stuhr_events.tsv', folder1_path+j+'/'+i+'/')
				os.rename(folder1_path+j+'/'+i+'/sub-XXX_task-stuhr_events.tsv',folder1_path+j+'/'+i+'/'+j+'_task-stuhr_events.tsv')

