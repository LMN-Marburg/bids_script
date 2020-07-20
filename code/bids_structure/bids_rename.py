import os
import pandas as pd
import shutil


# (1) TSV-File einlesen

bids_zuordnung = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/bids_zuordnung_dataset2_neu.tsv'

df = pd.read_csv(bids_zuordnung, sep='\t')

source = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

# (2) Rename folders to sub-xxx

cnt == 281
for ind, row in df.iterrows():

	os.rename(source+row['bids_id_new'],source+"sub-{:03d}".format(cnt))
	cnt += 1
