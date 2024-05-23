import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date

class Measurment_Path:
    def __init__(self, patient_path, folder_path):

        self.patient_path = patient_path

        if(None == folder_path):
            self.folder_path = self.make_measurment_folder()
        else:
            self.folder_path = folder_path

        #make folder

        self.patient_file_path = self.make_patient_path()
        self.raw_data_file = self.make_raw_path()

        self.make_patient_file()
        self.make_raw_file()

    def make_measurment_folder(self):
        today = date.today()
        name_prefix = "Measurment_" + today.strftime("%m-%d-%Y") + '_#'

        today_dirs = glob.glob(self.patient_path + '/' + name_prefix+'*')
        today_measurments = len(today_dirs)
        name = name_prefix + str(today_measurments + 1)

        folder_path = self.patient_path + '/' + name
        os.makedirs(folder_path)

        return folder_path

######################################################################
###################### MAKE PATHS ####################################

    def make_patient_path(self):
        return self.folder_path + '/patient.csv'

    def make_raw_path(self):
        return self.folder_path + '/raw_data.csv'

######################################################################
###################### MAKE FILES ####################################

    def make_patient_file(self):
        open(self.patient_file_path, 'a', newline='')

    def make_raw_file(self):
        open(self.raw_data_file, 'a', newline='')
