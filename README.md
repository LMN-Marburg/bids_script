# BIDS Script
Script to get data from the server into [BIDS](https://bids-specification.readthedocs.io/en/stable/).

## What it should do

- create the folder structure according to [BIDS](https://bids-specification.readthedocs.io/en/stable/) with folders for
  - functional MRI
  - structural MRI
  - fieldmaps
  - (DWI)
- merge functional files
- copy files in their respective folders
- for fieldmap data
  - get both echotimes and add them to the right json file

## What it does (so far)

General:

- creates folders for all subjects
- creates participants.tsv with the following columns:
  - `participant_id`: Subject ID as specified in BIDS
  - `server_id`: Subject ID that was assigned when getting the data from the server

Anatomical data:

- creates `anat` folder for each participant
- copies T1 weighted image to this folder
- renames this image according to BIDS criteria

## How to run it

This script can be run from the command line, with the following structure:

`python3 bids_script.py path/to/sourcedata path/to/bids_folder --task taskname --anat anatomical_naming_scheme --func functional_naming_scheme --fmap fieldmap_naming_scheme --normal`

From the help text of the script:

```
usage: Creates folders and copies files from imaging data set
    according to BIDS.

positional arguments:
  data         Absolute path to where the data are stored. The script expects
               all subfolders to be sub- jects with respective folders for the
               given modalities (string)
  bids_folder  Absolute path to the folder where the BIDS data should be
               stored (string)

optional arguments:
  -h, --help   show this help message and exit
  --task TASK  Name of the fMRI task
  --anat ANAT  Folder name of T1 image (without 00X__)
  --func FUNC  Folder name of functional images
  --fmap FMAP  Folder name of fieldmap images
  --normal     Should the prenormalized T1 image be used? Defaults to False if
               not specified
```
