import os
import sys
import json
import io
import shutil

## append phasediff json file: 2 instead of 1 echo times

#get folder where all the data is inside
#folder1_path = sys.argv[1]
folder1_path = '/scratch/face_lateralisation_LMN/StUHR_face/data/'

#all the subjects
folder1 = os.listdir(folder1_path)

#rename
for j in folder1:
	if os.path.isdir(folder1_path+j) and j.startswith('sub'):
	# and j.endswith(n for n in folder1_path+j if int(n.split('-')[-1]) > 280)
		#go to respective field map folder
		folder_in = folder1_path+j+'/fmap/'
		# if folder does not contain any field maps, print respective subject and continue
		if len(os.listdir(folder_in)) == 0:
			print (j+' does not have any field map data.')
			continue
		else:
			# (1) lese magnitude1.json, suche entsprechende EchoTime1
			mag1_file = open(folder_in+j+'_magnitude1.json')
			mag1_vars = json.load(mag1_file)
			et1 = mag1_vars["EchoTime"]
			mag1_file.close()
			# (2) lese magnitude2.json, suche entsprechende EchoTime2
			mag2_file = open(folder_in+j+'_magnitude2.json')
			mag2_vars = json.load(mag2_file)
			et2 = mag2_vars["EchoTime"]
			mag2_file.close()
			# (3) update phasediff.json with echo times
			echo_times = {"EchoTime1": et1, "EchoTime2": et2}
			# if permission denied (in old bids subjects up to sub-280), continue to new subs
			try:
				with open(folder_in+j+"_phasediff.json", "r+") as file:
    					data = json.load(file)
					file.seek(0)
					if not "EchoTime1" in data and not "EchoTime2" in data:
						print('Updating '+j+'_phasediff.json.')
    						data.update(echo_times)
						file.seek(0)
						json.dump(data, file, indent=2, sort_keys=True, separators=(',', ': ')).replace('\\n','\n')
			except: 
				#data.close()
				continue

