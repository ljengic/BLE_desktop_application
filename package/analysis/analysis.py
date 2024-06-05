import os
import sys
import pathlib

class Analysis():
    def __init__(self, measurment_path):

        self.measurment_path = measurment_path

        #tu se poziva analyis_path novi (sa putanjom None) 
        #- to ce stvorit folder i datoteke