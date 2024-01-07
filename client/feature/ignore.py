import cticf, server, sys, os, json
from pathlib import Path
file_path = Path(sys.argv[0]).parent.absolute()

with open(os.path.join(file_path, "options.json"), "r") as options_file:
    options = json.load(options_file)
    options_file.close()

ui = cticf.rfile(os.path.join(file_path, "feature/ignore.cticf"))
ui = {
    "message": ui[0]
}

def run():
    print("\n" + ui["message"] + "\n")

    options["skipped_update"] = server.needs_update()[1]
    with open(os.path.join(file_path, "options.json"), "w") as options_file:
        json.dump(options, options_file, separators=(",", ":"))