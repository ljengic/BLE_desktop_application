import os
import sys
import time
import pathlib
from datetime import date

def make_file(path):
    f = open(path, 'a', newline='')
    f.close()