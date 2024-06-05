import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date
from package.tools import write_to_file
from package.tools import scale_time

def decode_msg(measurment, msg):
    msg[1] = scale_time(msg[1])
    if("2" == msg[0]):
        parse_acceleration(measurment, msg[1:])

def parse_acceleration(measurment, msg):
    #print(msg)
    write_to_file(measurment.accel_x_path,[msg[0],msg[1]])
    write_to_file(measurment.accel_y_path,[msg[0],msg[2]])
    write_to_file(measurment.accel_z_path,[msg[0],msg[3]])