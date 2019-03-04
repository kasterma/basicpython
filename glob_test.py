# Playing with files: adding download dates to files in Downloads folder
#
# Tries to avoid adding date to files that already have a date added.

import glob
import os
import time
import shutil

ddir = "/Users/kasterma/Downloads/"

files = glob.glob(ddir + "*")
files_wd = glob.glob(ddir + "[0-9]*-[0-9]*--*")

tol_files = [f for f in files if f not in files_wd]

for file in tol_files:
    ss = os.stat(file)
    ct = time.gmtime(ss.st_ctime)
    print(file)
    print(os.path.dirname(file) + "/" + time.strftime("%m-%d", ct) + "--" + os.path.basename(file))
    shutil.move(file, os.path.dirname(file) + "/" + time.strftime("%m-%d", ct) + "--" + os.path.basename(file))