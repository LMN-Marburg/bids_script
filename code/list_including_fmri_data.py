import os
import pandas as pd
import shutil


# (1) TSV-File einlesen

bids_zuordnung = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/bids_zuordnung_dataset2.tsv'

df = pd.read_csv(bids_zuordnung, sep='\t')

# (2) Subjectnamen ohne fMRT-Daten auslesen

source = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/'

no_fmri = []

for ind, row in df.iterrows():

	# temp_list = Unterordner des entsprechenden subjects
	temp_list = os.listdir(source+row['bids_id'])
	fmri_exists = False	
	for i in temp_list:
					
		# look for subs without complete fmri measurement
		if ('ep2d_bold_log_' in i) and (len(os.listdir(source+row['bids_id']+'/'+i)) >= 532):
			# setze Flag, falls fMRT-Ordner vorhanden UND komplett
			fmri_exists = True

	# wenn flag false (i.e. fMRT-Ordner fehlend oder nicht komplett)
	if not fmri_exists:
		# schreibe in Liste
		no_fmri.append(row['bids_id'])
	

print(no_fmri) # vorher

no_fmri.append('S327') # +Strukturausschluss
no_fmri.sort()

print(no_fmri) # nachher			

# (3) Neuen Dataframe bauen mit zusaetzlicher Spalte fuer neue BIDS-ID (=df_new) bzw. Ergaenzung des existierenden Dataframes (=df)

df_new = pd.DataFrame(columns=['raw_data_id', 'bids_id', 'bids_id_new'])

df.insert(2, "bids_id_new", "")

cnt = 281 # count fuer neue BIDS_ID (Start bei S281)

for ind, row in df.iterrows():

	if row['bids_id'] in no_fmri:
		# loesche den entsprechend unvollstaendigen Subject-Ordner
		shutil.rmtree(source+row['bids_id'])

	else:
		bids_id_new = "S{:03d}".format(cnt) # benenne weiter
		cnt+=1
		df.loc[ind] = [row['raw_data_id'], row['bids_id'], bids_id_new] # schreibe die Zeile in den Dataframe
		df_new.loc[ind] = [row['raw_data_id'], row['bids_id'], bids_id_new]
		os.rename(source+row['bids_id'],source+row['bids_id_new']) # geloeschte Subjectnummer wird neu vergeben
		
# Speichern der neuen Zuordnungs-Liste(n)
#df.to_csv('bids_zuordnung_neu_mit_luecken.tsv', sep = '\t', index = False)
df_new.to_csv('bids_zuordnung_dataset2_neu.tsv', sep = '\t', index = False)


