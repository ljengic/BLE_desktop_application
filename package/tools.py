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

def write_max_to_file(path, msg):
    with open( path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(msg)
        file.close()

def get_max_from_csv(path):
    rows = []

    with open( path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
        file.close()

    print(rows[0])

def scale_time(value):
    integer = int(value)
    decimal = float(integer/1000)
    return str(decimal)