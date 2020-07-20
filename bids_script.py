def run(data, bids_folder, anat = True, func = True, fieldmap = True):
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
    anatfolder = input("")#texteingabe
    funcfolder = #texteingabe
    fieldmapfolder = #texteingabe
<<<<<<< HEAD
    subjects = os.listdir()#count folders in data folder
=======
    subjects = os.listdir(data)#list of subject folders in data folder
>>>>>>> d3ab2d5ba4407a5008aef5da97e195b6699a0e6a
    for sub, index in zip(subjects, range(len(subjects)):
        sublabel = "{:03d}".format(index+1)

        anatfun(anatfolder=anatfolder, bids_folder= bids_folder, sub=sublabel,
                subfolder = sub)
        funcfun()
        fieldmapfun()

def anatfun(anatfolder, bids_folder, sub, subfolder):
    import os
    os.chdir()
    pass

def funcfun(data):
    pass

def fieldmapfun(arg):
    pass
