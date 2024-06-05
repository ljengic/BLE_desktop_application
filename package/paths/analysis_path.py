import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date

class Measurment_Path:
    def __init__(self, measurment_path, folder_path):

        self.measurment_path = measurment_path

        if(None == folder_path):
            self.folder_path = self.make_measurment_folder()
        else:
            self.folder_path = folder_path


    #   make paths

    #   make files

    def make_analysis_folder(self):
        name = "Analysis"

        folder_path = self.measurment_path + '/' + name
        os.makedirs(folder_path)

        return folder_path

######################################################################
###################### MAKE PATHS ####################################

#   make paths