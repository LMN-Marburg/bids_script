import os
import sys
import subprocess

## rename anat data

#get folder where all the Data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/test/'

#all the sessions
folder1 = os.listdir(folder1_path)

#rename
for j in folder1:
	print(j)
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):	
		#list all sequences 
		folder_in = os.listdir(folder1_path+j)
		#for every sequence	
		temp_t1_list=[]
		for i in folder_in:
			#look for the two t1 measurements and choose the first one (unnormalized)
			if 't1' in i and not i.startswith('_') and not i.startswith('1'):
				temp_t1_list.append(i)
		if len(temp_t1_list)==2:
			print(temp_t1_list)
			value_1 = temp_t1_list[0].split('__t1')[0]
			value_2 = temp_t1_list[1].split('__t1')[0]
			#print ('value 1: ' + value_1 + ' value 2: ' + value_2) 
			t1_value = ''		
			if value_1 < value_2: 
				t1_value = temp_t1_list[0]
			else: 
				t1_value = temp_t1_list[1]
			
			# name of the folder you want to have 
			print (j+': '+t1_value)
	
			os.rename(folder1_path+j+'/'+t1_value+'/bids.json',folder1_path+j+'/'+t1_value+'/'+j+'_T1w.json')
			os.rename(folder1_path+j+'/'+t1_value,folder1_path+j+'/'+'anat')
			for filename in os.listdir(folder1_path+j+'/anat/'):
    				if filename.startswith("t1mprsagp2iso"):
        				old_path = os.path.join(folder1_path+j+'/anat/', filename)
        				os.rename(old_path, folder1_path+j+'/anat/'+j+'_T1w.nii')

