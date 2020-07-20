import os
import pandas as pd
import shutil

bids_zuordnung = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/bids_zuordnung_dataset2.tsv'

df = pd.read_csv(bids_zuordnung, sep='\t')

source = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/'

underscore = []

for ind, row in df.iterrows():

	# temp_list = Unterordner des entsprechenden subjects
	temp_list = os.listdir(source+row['bids_id'])
	underscore_exists = False	
	for i in temp_list:
					
		# look for subs without complete fmri measurement
		if (i[0]=='_'):
			# setze Flag, falls fMRT-Ordner vorhanden UND komplett
			underscore_exists = True

	# wenn flag false (i.e. fMRT-Ordner fehlend oder nicht komplett)
	if underscore_exists:
		# schreibe in Liste
		underscore.append(row['bids_id'])
	

print(underscore) 
