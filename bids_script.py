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
    subjects = os.#count folders in data folder
    for sub, index in zip(subjects, range(len(subjects)):
        if index < 9:
            sublabel = f"00{index+1}"
        if index > 8 and index < 99:
            sublabel = f"0{index+1}"
        else:
            sublabel = f"{index+1}"

        anatfun(sub=sublabel)
        funcfun()
        fieldmapfun()

def anatfun(anatfolder, sub):
    import os

    pass

def funcfun(data):
    pass

def fieldmapfun(arg):
    pass
