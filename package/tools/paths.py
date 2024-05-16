import sys
import time

class Paths:
    def __init__(self, folder_path):
        self.folder_path = folder_path

        self.patient_file_path = self.make_patient_path()
        self.temp_data_file = self.make_temp_path()
        self.bioz_data_file_frek = self.make_bioz_path_frek()
        self.bioz_data_file_5 = self.make_bioz_path_5()
        self.bioz_data_file_50 = self.make_bioz_path_50()
        self.bioz_data_file_100 = self.make_bioz_path_100()
        self.bioz_data_file_200 = self.make_bioz_path_200()
        self.raw_data_file = self.make_raw_path()


        self.make_patient_file()
        self.make_temp_file()
        self.make_bioz_file_frek()
        self.make_bioz_file_5()
        self.make_bioz_file_50()
        self.make_bioz_file_100()
        self.make_bioz_file_200()
        self.make_raw_file()

######################################################################
###################### MAKE PATHS ####################################

    def make_patient_path(self):
        return self.folder_path + '/patient.csv'

    def make_temp_path(self):
        return self.folder_path + '/temp_data.csv'

    def make_bioz_path_frek(self):
        return self.folder_path + '/bioz_data_frek.csv'

    def make_bioz_path_5(self):
        return self.folder_path + '/bioz_data_5.csv'

    def make_bioz_path_50(self):
        return self.folder_path + '/bioz_data_50.csv'

    def make_bioz_path_100(self):
        return self.folder_path + '/bioz_data_100.csv'

    def make_bioz_path_200(self):
        return self.folder_path + '/bioz_data_200.csv'

    def make_raw_path(self):
        return self.folder_path + '/raw_data.csv'

######################################################################
###################### MAKE FILES ####################################

    def make_patient_file(self):
        open(self.patient_file_path, 'a', newline='')

    def make_temp_file(self):
        open( self.temp_data_file, 'a', newline='')

    def make_bioz_file_frek(self):
        open( self.bioz_data_file_frek, 'a', newline='')

    def make_bioz_file_5(self):
        open( self.bioz_data_file_5, 'a', newline='')

    def make_bioz_file_50(self):
        open( self.bioz_data_file_50, 'a', newline='')

    def make_bioz_file_100(self):
        open( self.bioz_data_file_100, 'a', newline='')

    def make_bioz_file_200(self):
        open( self.bioz_data_file_200, 'a', newline='')

    def make_raw_file(self):
        open(self.raw_data_file, 'a', newline='')
