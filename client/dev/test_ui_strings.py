# Might only work on Windows

from pathlib import Path
import cticf, sys, os

path = Path(sys.argv[0]).parent.parent.absolute()

files = []

for file in os.listdir(path):
    if file.endswith(".cticf"):
        files.append(os.path.join(path, file))
        
for file in files:
    for string in cticf.rfile(file):
        print(string)