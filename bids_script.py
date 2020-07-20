def run(data, bids_folder, anat = True, func = True, fieldmap = True,
        normalized = True):
    """
    Creates folders and copies files according to BIDS.
    Arguments:
        data: absolute path to where the data are stored. The script expects all
        subfolders to be subjects with respective folders for the given modali-
        ties (string)
        bids_folder: absolute path to the folder where the BIDS data will be
        stored (string)
        anat: Is there anatomical data? (bool)
        func: Is there functional data? (bool)
        fieldmap: Is there fieldmap data? (bool)
        normalized: Should the prenormalized T1 image be used? (bool)
    """
    import os
    if anat == True:
        anatfolder = input("Folder name of T1 image (without 00X__)")
    if func == True:
        funcfolder = input("Folder name of functional images:")
    if fieldmap == True:
        fieldmapfolder = input("Folder name of fieldmap images:")
    taskname = input("Name of the fMRI task:")
    subjects = os.listdir(data) #list of subject folders in data folder

    for sub, index in zip(subjects, range(len(subjects)):
        sublabel = "{:03d}".format(index+1)
        # create folders for existing modalities
        os.chdir(bids_folder)
        os.mkdir(f"sub-{sublabel}")
        os.chdir(f"sub-{sublabel}")
        if anat == True:
            os.mkdir("anat")
            anatfun(data=data, anatfolder=anatfolder, bids_folder= bids_folder
            sublabel=sublabel, subfolder = sub, bids_subfolder = f"sub-{sublabel}",
            normalized = normalized)
        if func == True:
            os.mkdir("func")
        if fieldmap == True:
            os.mkdir("fmap")
        # TODO: save old subject names in participants.tsv

        funcfun()
        fieldmapfun()

def anatfun(data, anatfolder, bids_folder, sublabel, subfolder, bids_subfolder,
            normalized):
    import os
    import shutil
    import json
    # which folder contains the right T1 image? (normalized or not normalized)
    abs_bids_subfolder = os.path.join(bids_folder, bids_subfolder)
    modalities = os.listdir(abs_bids_subfolder)
    # go through all anatomical folders
    for mod in modalities:
        # does the string match the anat folder name?
        if anatfolder in mod:
            # change working directory to this folder
            os.chdir(os.path.join(abs_bids_subfolder, mod))
            # open json file
            with open("bids.json") as json_file:
                metadata = json.load(json_file)
                # does list ImageType contain "NORM?"
                if metadata["ImageType"][-1] == "NORM" and normalized == True:
                    sourcefolder = mod
                elif metadata["ImageType"][-1] != "NORM" and normalized == False:
                    sourcefolder = mod


    # copy and rename T1-image
    source = os.path.join(data, subfolder, sourcefolder)
    target = os.path.join(bids_folder, bids_subfolder, anat,
                          f"sub-{sublabel}_T1w.nii")
    shutil.copy(source, target)

def funcfun(data):
    pass

def fieldmapfun(arg):
    pass
