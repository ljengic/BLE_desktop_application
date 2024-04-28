import sys
import time

class Paths:
    def __init__(self, folder_path):
        self.folder_path = folder_path

        self.patient_file_path = self.make_patient_path()
        self.temp_data_file = self.make_temp_path()
        self.raw_data_file = self.make_raw_path()

        self.make_patient_file()
        self.make_temp_file()
        self.make_raw_file()

######################################################################
###################### MAKE PATHS ####################################

    def make_patient_path(self):
        return self.folder_path + '/patient.csv'

    def make_temp_path(self):
        return self.folder_path + '/temp_data.csv'

    def make_raw_path(self):
        return self.folder_path + '/raw_data.csv'

######################################################################
###################### MAKE FILES ####################################

    def make_patient_file(self):
        open(self.patient_file_path, 'a', newline='')

    def make_temp_file(self):
        open( self.temp_data_file, 'a', newline='')

    def make_raw_file(self):
        open(self.raw_data_file, 'a', newline='')
