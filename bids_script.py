def run(data, bids_folder, anat = True, func = True, fieldmap = True, normalized = True):
    """
    Creates folders and copies files according to BIDS.
    Arguments:
        data: absolute path to where the data are stored. The script expects all
        subfolders to be subjects with respective folders for the given modali-
        ties (string)
        bids_folder: absolute path to the folder where the BIDS data will be
        stored (string)
        anat: Is there anatomical data (bool)?
        func: Is there functional data (bool)?
        fieldmap: Is there fieldmap data (bool)?
    """
    import os
    if anat = True:
        anatfolder = input("Folder name of T1 image:")
    if func = True:
        funcfolder = input("Folder name of functional images:")
    if fieldmap = True:
        fieldmapfolder = input("Folder name of fieldmap images:")
    taskname = input("Name of the fMRI task:")
    subjects = os.listdir(data) #list of subject folders in data folder

    for sub, index in zip(subjects, range(len(subjects)):
        sublabel = "{:03d}".format(index+1)
        # create folders for existing modalities
        os.chdir(bids_folder)
        os.mkdir(f"sub-{sublabel}")
        os.chdir(f"sub-{sublabel}")
        if anat = True:
            os.mkdir("anat")
            anatfun(data=data, anatfolder=anatfolder, bids_folder= bids_folder, sublabel=sublabel,
                    subfolder = sub, bids_subfolder = f"sub-{sublabel}")
        if func = True:
            os.mkdir("func")
        if fieldmap = True:
            os.mkdir("fmap")
        # TODO: save old subject names in participants.tsv

        funcfun()
        fieldmapfun()

def anatfun(data, anatfolder, bids_folder, sublabel, subfolder, bids_subfolder):
    import os
    import shutil
    # copy and rename T1-image
    source = os.path.join(data, subfolder, anatfolder)
    target = os.path.join(bids_folder, bids_subfolder, anat, f"sub-{sublabel}_T1w.nii")
    shutil.copy(source, target)

    pass

def funcfun(data):
    pass

def fieldmapfun(arg):
    pass
