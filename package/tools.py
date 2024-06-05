import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date
from PyQt5 import QtWidgets, QtCore, QtGui

def set_window_icon_and_title(window):
    window.setWindowIcon(QtGui.QIcon('./images/logo.jpeg'))
    window.setWindowTitle("Fluid Track")

def write_to_file(path, msg):
    with open( path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(msg)
        file.close()  

def scale_time(value):
    integer = int(value)
    decimal = float(integer/1000)
    return str(decimal)