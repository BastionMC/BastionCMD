import cticf, os, sys
from pathlib import Path
file_path = Path(sys.argv[0]).parent.absolute()

ui = cticf.rfile(os.path.join(file_path, "feature/help.cticf"))
ui = {
    "list": ui[0]
}

def run():
    print("\n" + ui["list"] + "\n")