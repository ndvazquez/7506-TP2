from os import listdir
from os.path import isfile, join
import os, sys
import time

#jupyter nbconvert --to notebook --execute mynotebook.ipynb


"""
help:
    - "python autorun.py <dir_name>" runs every notebook in <dir>
    - "python autorun.py <file>.ipybn" runs that single notebook
    - "python autorun.py" runs every notebook in current dir
"""

# check the file that has the records of previously ran notebooks
try:
    previous_run = [n for n in open('.autorun_prev.txt')]
except FileNotFoundError:
    previous_run = []

path = os.getcwd()

# parse argv to know if a single fil should be run
if len(sys.argv) > 1:
    arg = sys.argv[1]
    try:
        if arg.split('.')[1] == 'ipynb': # if a .ipynb file is passed, I only execute that one
            os.system('jupyter nbconvert --to notebook --execute ' + path + arg)
            sys.exit()
    except IndexError:
        pass
    path += sys.argv[1]

files = [f for f in listdir(path) if isfile(join(path, f))]
notebooks = [f for f in files if f.split('.')[1]=='ipynb']
notebooks = [f for f in notebooks if f not in previous_run]  # I get the ones that are new

with open('.autorun_prev.txt', 'a+') as f:
    for n in notebooks:
        if n not in previous_run:
            f.write('\n' + n)

command = 'jupyter nbconvert --execute '

start = time.time()
i = 0
for notebook in notebooks:
    os.system(command + notebook)
    i += 1
end = time.time()

print()
print('{} notebooks were ran in {:.2f} seconds'.format(i, end-start))
print('No more noteboks to run')
