import os
import sys
import subprocess

## rename folder

#get folder where all the Data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

#all the sessions
folder1 = os.listdir(folder1_path)

#the logfile. this path has to be changed
out_file = open('/scratch/face_lateralisation_LMN/StUHR_face/data/logfile_merge_func.txt','a')

# rename folders into sub-XXX
for name in folder1:
	if name.startswith('S'):
		os.rename(os.path.join(folder1_path,name), os.path.join(folder1_path, name.replace('S', 'sub-')))

## merge and rename func data

#get folder where all the Data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

#all the sessions
folder1 = os.listdir(folder1_path)

#loop over all given Sessions
for j in folder1:
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):
		#list all sequences 
		folder_in = os.listdir(folder1_path+j)
		#for every sequence	
		for i in folder_in:
			#look for the epi sequence
			if i.find('ep2d_bold') > -1:
				count = len(os.listdir(folder1_path+j+'/'+i+'/'))
				if count < 531:
					pass
				else:
					#temp = os.listdir(folder1_path+j+'/'+i+'/')
					#print temp
					#for k in temp:
					#	if '_' in k and k.endswith('.nii'):
					#		os.remove(folder1_path+j+'/'+i+'/'+k)
					#start the conversion
					data = '/imaging/_data/face_lateralisation_LMN/StUHR_face/scripts/Datenset_2/bids_structure/merge_epi_NIfTI.sh '+ folder1_path+j+'/'+i+'/ out.nii'
					#output_file = folder1_path+j+'/'+i+'/' +j+ '.nii'
					#filt = folder1_path+j+'/'+i+'/*.nii'
					#os.system('fslmerge -t output_file data')
					out_file.write(j + '\n')
					os.system(data)

					# wohl sinnlos:
					for fname in os.listdir(folder1_path+j+'/'+i+'/'):
    						if fname.startswith('ep2dbold'):
        						os.remove(os.path.join(folder1_path+j+'/'+i+'/', fname))
	else:
		pass


#rename
for j in folder1:
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):	
		#list all sequences 
		folder_in = os.listdir(folder1_path+j)
		#for every sequence	
		for i in folder_in:
			#look for the epi sequence
			if i.find('ep2d_bold') > -1 and not i.startswith('_') and not os.path.exists(folder1_path+j+'/'+i+'/'+j+'_task-stuhr_bold.nii.gz'):
#or not os.path.exists(folder1_path+j+'/'+i+'/'+j+'_task-stuhr_bold.json') or not os.path.exists(folder1_path+j+'/'+'func'):
				print('Renaming bids.json, func images and folder name: '+j)
				os.rename(folder1_path+j+'/'+i+'/out.nii.gz',folder1_path+j+'/'+i+'/'+j+'_task-stuhr_bold.nii.gz')
				os.rename(folder1_path+j+'/'+i+'/bids.json',folder1_path+j+'/'+i+'/'+j+'_task-stuhr_bold.json')
				os.rename(folder1_path+j+'/'+i,folder1_path+j+'/'+'func')

