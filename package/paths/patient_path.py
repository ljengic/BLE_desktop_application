import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date
from package.paths.make_file import make_file

class Patient_Path:
    def __init__(self, folder_path):

        if(None == folder_path):
            self.folder_path = self.make_patient_folder()
        else:
            self.folder_path = folder_path

        self.name = self.folder_path.split('\\')[-1]

        self.patient_file_path = self.make_patient_path()

        make_file(self.patient_file_path)

    #make folder for patient
    def make_patient_folder(self):
        today = date.today()
        name_prefix = "Patient" + '_#'

        all_patients = glob.glob('data/'+name_prefix+'*')
        new_patient = len(all_patients) +1
        name = name_prefix + str(new_patient)

        folder_path = os.getcwd() + "\data\\" + name
        os.makedirs(folder_path)

        return folder_path

######################################################################
###################### MAKE PATHS ####################################

    def make_patient_path(self):
        return self.folder_path + '/patient.csv'
