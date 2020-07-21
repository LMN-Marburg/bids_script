#!/usr/bin/env python

import os
import shutil
import json
from argparse import ArgumentParser


def anatfun(data, anatfolder, bids_folder, sublabel, subfolder, bids_subfolder,
            normalized):
    # which folder contains the right T1 image? (normalized or not normalized)
    modalities = os.listdir(os.path.join(data, subfolder))
    # go through all anatomical folders
    for mod in modalities:
        # does the string match the anat folder name?
        if anatfolder in mod:
            # change working directory to this folder
            os.chdir(os.path.join(data, subfolder, mod))
            # open json file
            with open("bids.json") as json_file:
                metadata = json.load(json_file)
            # does list ImageType contain "NORM?"
            if normalized == True:
                if metadata["ImageType"][-1] == "NORM":
                    sourcefolder = mod
                    print("Normalized image found")
            else:
                if metadata["ImageType"][-1] != "NORM":
                    print("Unnormalized image found")
                    sourcefolder = mod
    # find the nii file
    anatfiles = os.listdir(os.path.join(data, subfolder, mod))
    sourcefile = None
    for f in anatfiles:
        if ".nii" in f:
            sourcefile = f
    if sourcefile == None:
        raise FileNotFoundError("No .nii file found")
    #copy and rename T1-image

    source = os.path.join(data, subfolder, mod, sourcefile)
    target = os.path.join(bids_folder, bids_subfolder, "anat",
                         f"sub-{sublabel}_T1w.nii")
    print(f"Copying T1 image of subject {sublabel}")
    shutil.copy(source, target)

    return(None)


def funcfun(data):
    pass


def fieldmapfun(arg):
    pass


def run(data, bids_folder, anat, func, fieldmap, normalized, task):
    """
    Creates folders and copies files according to BIDS.
    Arguments:
        data: absolute path to where the data are stored. The script expects all
        subfolders to be subjects with respective folders for the given modali-
        ties (str)
        bids_folder: absolute path to the folder where the BIDS data will be
        stored (str)
        anat: Folder name of T1 image (without 00X__) (str)
        func: Folder name of functional images (str)
        fieldmap: Folder name of fieldmap images (str)
        normalized: Should the prenormalized T1 image be used? (bool)
    """
    if anat != None:
        anatexists = True
    else:
        anatexists = False
    if func != None:
        funcexists = True
    else:
        funcexists = False
    if fieldmap != None:
        fieldmapexists = True
    else:
        fieldmapexists = False

    subjects = os.listdir(data) #list of subject folders in data folder

    for sub, index in zip(subjects, range(len(subjects))):
        sublabel = "{:03d}".format(index+1)
        # create folders for existing modalities
        os.chdir(bids_folder)
        # if os.path.exists(os.path.join(bids_folder, f"sub-{sublabel}")) == False:
        #     print(os.path.join(bids_folder, f"sub-{sublabel}"))
        try:
            os.mkdir(f"sub-{sublabel}")
            os.chdir(f"sub-{sublabel}")
        except FileExistsError:
            print(f"Data for subject {sublabel} already exists")
            continue
        if anatexists == True:
            os.mkdir("anat")
            anatfun(data=data, anatfolder=anat, bids_folder= bids_folder,
            sublabel=sublabel, subfolder = sub, bids_subfolder = f"sub-{sublabel}",
            normalized = normalized)
        if funcexists == True:
            os.mkdir("func")
            funcfun()
        if fieldmapexists == True:
            os.mkdir("fmap")
            fieldmapfun()
        # TODO: save old subject names in participants.tsv
    return(None)


def main():
    description = """Creates folders and copies files from imaging data set
    according to BIDS."""
    parser = ArgumentParser(__file__, description)
    parser.add_argument("data", action="store", help = """Absolute path to
    where the data are stored. The script expects all subfolders to be sub-
    jects with respective folders for the given modalities (string)""",
    type = str)
    parser.add_argument("bids_folder", action="store", help = """Absolute
    path to the folder where the BIDS data should be stored (string)""",
    type = str)
    parser.add_argument("--task", action="store", help="Name of the fMRI task",
    type=str)
    parser.add_argument("--anat", help="Folder name of T1 image (without 00X__)",
    action="store", type=str)
    parser.add_argument("--func", help="Folder name of functional images",
    action="store", type=str)
    parser.add_argument("--fmap", help="Folder name of fieldmap images",
    action="store", type=str)
    parser.add_argument("--normal", help="""Should the prenormalized T1 image be
    used? Defaults to False if not specified""", action="store_true")
    args = parser.parse_args()

    run(data=args.data, bids_folder=args.bids_folder, anat = args.anat, func =
    args.func, fieldmap = args.fmap, normalized = args.normal,
    task = args.task)
    return(None)


if __name__ == '__main__':
    main()
