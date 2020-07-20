import os
import sys
import subprocess
import shutil

## copy and rename fmap data

#get folder where all the Data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

#all the sessions
folder1 = os.listdir(folder1_path)

#rename
for j in folder1:
	print(j)
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):
		temp_fmap_list=[]
		#create fmap folder which will be filled with mag1, mag2, phasediff
		if os.path.exists(folder1_path+j+'/fmap'):
			pass
		else:
			os.mkdir(folder1_path+j+'/fmap')	
		#list all sequences 
		folder_in = os.listdir(folder1_path+j)	
		for i in folder_in:
			#look for the two gre_field measurements and choose magnitude1+2 from first folder and phasediff from second folder
			if 'gre_field' in i and not i.startswith('_'):
				temp_fmap_list.append(i)
				temp_fmap_list.sort()
			print(temp_fmap_list)
		if len(temp_fmap_list)<2:
			print(j+' has less than 2 gre_field_mapping folders. Check manually.')
		else:
			#print(temp_fmap_list)
			mag_folder = temp_fmap_list[0]
			phdiff_folder = temp_fmap_list[1]

			##copy and rename magnitude files
			#bids_e1.json
			shutil.copy(folder1_path+j+'/'+mag_folder+'/bids_e1.json',folder1_path+j+'/fmap/')
			os.rename(folder1_path+j+'/fmap/bids_e1.json',folder1_path+j+'/fmap/'+j+'_magnitude1.json')
			#bids_e2.json
			shutil.copy(folder1_path+j+'/'+mag_folder+'/bids_e2.json',folder1_path+j+'/fmap/')
			os.rename(folder1_path+j+'/fmap/bids_e2.json',folder1_path+j+'/fmap/'+j+'_magnitude2.json')
			#grefieldmapping_1.nii
			for filename in os.listdir(folder1_path+j+'/'+mag_folder+'/'):
    				if filename.startswith("grefieldmapping") and filename.endswith("_1.nii"):
					shutil.copy(folder1_path+j+'/'+mag_folder+'/'+filename, folder1_path+j+'/fmap/')
        				old_path = os.path.join(folder1_path+j+'/fmap/', filename)
        				os.rename(old_path, folder1_path+j+'/fmap/'+j+'_magnitude1.nii')
			#grefieldmapping_2.nii
			for filename in os.listdir(folder1_path+j+'/'+mag_folder+'/'):
    				if filename.startswith("grefieldmapping") and filename.endswith("_2.nii"):
					shutil.copy(folder1_path+j+'/'+mag_folder+'/'+filename, folder1_path+j+'/fmap/')
        				old_path = os.path.join(folder1_path+j+'/fmap/', filename)
        				os.rename(old_path, folder1_path+j+'/fmap/'+j+'_magnitude2.nii')

			##copy and rename phasediff files
			#bids_e2_ph.json
			shutil.copy(folder1_path+j+'/'+phdiff_folder+'/bids_e2_ph.json',folder1_path+j+'/fmap/')
			os.rename(folder1_path+j+'/fmap/bids_e2_ph.json',folder1_path+j+'/fmap/'+j+'_phasediff.json')
			#grefieldmapping.nii
			for filename in os.listdir(folder1_path+j+'/'+phdiff_folder+'/'):
    				if filename.startswith("grefieldmapping") and filename.endswith("001.nii"):
					shutil.copy(folder1_path+j+'/'+phdiff_folder+'/'+filename, folder1_path+j+'/fmap/')
        				old_path = os.path.join(folder1_path+j+'/fmap/', filename)
        				os.rename(old_path, folder1_path+j+'/fmap/'+j+'_phasediff.nii')

