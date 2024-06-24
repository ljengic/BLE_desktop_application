import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date
from package.paths.make_file import make_file

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

        self.accel_x_path = self.make_accel_x_path()
        self.accel_y_path = self.make_accel_y_path()
        self.accel_z_path = self.make_accel_z_path()

        self.bioz_5_path = self.make_bioz_5_path()
        self.bioz_50_path = self.make_bioz_50_path()
        self.bioz_100_path = self.make_bioz_100_path()
        self.bioz_200_path = self.make_bioz_200_path()

        self.bioz_max_path = self.make_bioz_max_path()

        make_file(self.patient_file_path)
        make_file(self.raw_data_file)

        make_file(self.accel_x_path)
        make_file(self.accel_y_path)
        make_file(self.accel_z_path)

        make_file(self.bioz_5_path)
        make_file(self.bioz_50_path)
        make_file(self.bioz_100_path)
        make_file(self.bioz_200_path)

        make_file(self.bioz_max_path)

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

    def make_accel_x_path(self):
        return self.folder_path + '/accel_x.csv'

    def make_accel_y_path(self):
        return self.folder_path + '/accel_y.csv'  

    def make_accel_z_path(self):
        return self.folder_path + '/accel_z.csv'

    def make_bioz_5_path(self):
        return self.folder_path + '/bioz_5.csv'

    def make_bioz_50_path(self):
        return self.folder_path + '/bioz_50.csv'

    def make_bioz_100_path(self):
        return self.folder_path + '/bioz_100.csv'

    def make_bioz_200_path(self):
        return self.folder_path + '/bioz_200.csv'

    def make_bioz_max_path(self):
        return self.folder_path + '/bioz_max.csv'
          