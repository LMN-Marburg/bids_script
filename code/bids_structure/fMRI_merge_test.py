import __future__ 
import fileinput, glob, string, sys, os, re
import pandas as pd
import shutil

bids_zuordnung = '/scratch/face_lateralisation_LMN/StUHR_face/data/sourcedata/bids_zuordnung_dataset2_neu.tsv'
df = pd.read_csv(bids_zuordnung, sep='\t')

source = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

# (4) fMRT

# merge files (fslmerge -t)

os.system("fsl5env") # alternativ im Terminal aufrufen und danach Skript starten

os.walk("/scratch/face_lateralisation_LMN/StUHR_face/data/S281")

# cnt = 281
# for ind, row in df.iterrows():
# for ((files)) in "/scratch/face_lateralisation_LMN/StUHR_face/data/sub-{:03d}".format(row['bids_id_new'])

def checkdirnames(name):
	# check if directory name matches with given pattern
	pattern = re.compile('019__ep2d_bold')
	m = pattern.search(name)
	if m is None:
		return False
	else:
		return True


# walk a directory tree, using a generator, rename certain directories
newname = 'newdir'
for f in os.listdir(dir):
	fullpath = os.path.join(dir,f)
		
	if checkdirname(f):
		os.rename(fullpath,os.path.join(dir,'func'))
