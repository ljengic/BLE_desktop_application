import os
import sys
import time
import csv
import pathlib
import glob
import sip
import math
from datetime import date
from package.tools import write_max_to_file
from package.tools import write_to_file
from package.tools import scale_time

def decode_msg(measurment, msg):
    msg[1] = scale_time(msg[1])
    if("2" == msg[0]):
        parse_acceleration(measurment, msg[1:])
    elif("0" == msg[0]):
        parse_bioz(measurment, msg[1:])  

def parse_acceleration(measurment, msg):
    #print(msg)
    write_to_file(measurment.accel_x_path,[msg[0],msg[1]])
    write_to_file(measurment.accel_y_path,[msg[0],msg[2]])
    write_to_file(measurment.accel_z_path,[msg[0],msg[3]])

def parse_bioz(measurment, msg):

    real = float(msg[2])
    imag = float(msg[3])

    mag = math.sqrt(real*real + imag*imag)

    if("5" == msg[1]):
        write_to_file(measurment.bioz_5_path,[msg[0],mag])
    elif("50" == msg[1]):
        write_to_file(measurment.bioz_50_path,[msg[0],mag])
    elif("100" == msg[1]):
        write_to_file(measurment.bioz_100_path,[msg[0],mag])
    elif("200" == msg[1]):
        write_to_file(measurment.bioz_200_path,[msg[0],mag])

    write_max_to_file(measurment.bioz_max_path,[msg[0],mag])  