import os
import pandas as pd
import shutil

# (1) Zuordnungs-Tabelle

df = pd.DataFrame(columns=['raw_data_id', 'bids_id'])

dcm_folder_list = os.listdir('/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/Psychiatrie^Nenadic/sourcedata_20191016-20200226/')

for i in range(len(dcm_folder_list)):
	raw_data_id = dcm_folder_list[i]
	bids_id = "S{:03d}".format(i+281)
	df.loc[i] = [raw_data_id, bids_id]

df.to_csv('bids_zuordnung_dataset2.tsv', sep = '\t', index = False)


# (2) Zuordnung source zu destination

source = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/Psychiatrie^Nenadic/sourcedata_20191016-20200226/'

destination = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/'

for ind, row in df.iterrows():
	# create a folder with bids id
	if not os.path.exists(destination + row['bids_id']):
		os.mkdir(destination + row['bids_id'])

	# look for the needed data
	temp_list = os.listdir(source+row['raw_data_id'])
	for i in temp_list:
		#both t1
		if 't1_' in i:
			shutil.copytree(source+row['raw_data_id']+'/'+i, destination+row['bids_id']+'/'+i)				
		# fmri
		elif 'ep2d_bold_log_' in i:
			shutil.copytree(source+row['raw_data_id']+'/'+i, destination+row['bids_id']+'/'+i)				
		#maps
		elif i.endswith('gre_field_mapping'):
			shutil.copytree(source+row['raw_data_id']+'/'+i, destination+row['bids_id']+'/'+i)				

