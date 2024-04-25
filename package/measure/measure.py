import os
import sys
import time
import csv
import pathlib
import glob
from datetime import date
from PyQt5 import QtWidgets, QtCore
from package.measure.gui_measure import Ui_Measure
from package.ble.ble import BLE

class Measure(QtWidgets.QWidget, Ui_Measure):

    def __init__(self,ble_instance):
        super(Measure, self).__init__()
        self.setupUi(self)

        self.ble = ble_instance

        self.btn_start.clicked.connect(self.btn_start_press_handle)
        self.btn_stop.clicked.connect(self.btn_stop_press_handle)
        self.ble.ble_msg_received.connect(self.msg_received)

    def msg_received(self, msg):
        msg_list = msg.split(';') 
        self.csv_write_raw_data(msg_list)
        self.decode_msg(msg_list)

    def csv_write_raw_data(self, data):
        #change this later, there is no need for opening the file every time

        self.raw_data_file = self.folder_path + '/raw_data.csv'
        with open(self.raw_data_file, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(data)
            file.close()

    def decode_msg(self,msg):
        print(msg)
        if('0' == msg[1]):
            self.csv_write_bioz_data(msg)
        elif('1' == msg[1]):
            self.csv_write_temperature_data(msg)    
        else:
            print("ERROR: cannot decode received data")            

    def csv_write_temperature_data(self,msg):
        print("Received data from temperature sensor.")
        self.temp_data_file = self.folder_path + '/temp_data.csv'
        with open( self.temp_data_file, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([msg[0],msg[2]])
            file.close()

    def csv_write_bioz_data(self,msg):
        print("Received data from bioz sensor.")

    def btn_start_press_handle(self):
        self.make_measurment_folder()
        self.ble.ble_send(3)

    def btn_stop_press_handle(self):
        self.ble.ble_send(4)

    #make folder for this measurment
    def make_measurment_folder(self):
        today = date.today()
        name_prefix = "Measurment_" + today.strftime("%m-%d-%Y") + '_#'

        today_dirs = glob.glob('data/'+name_prefix+'*')
        today_measurments = len(today_dirs)
        name = name_prefix + str(today_measurments + 1)

        self.folder_path = os.getcwd() + "\data\\" + name
        os.makedirs(self.folder_path)
