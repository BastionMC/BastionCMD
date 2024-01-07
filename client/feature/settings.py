import json, cticf, formatting, os, sys
from pathlib import Path
file_path = Path(sys.argv[0]).parent.absolute()

with open(os.path.join(file_path, "options.json"), "r") as options_file:
    options = json.load(options_file)
    options_file.close()

ui = cticf.rfile(os.path.join(file_path, "feature/settings.cticf"))
ui = {
    "divider": ui[0],
    "prompt": ui[1],
    "invalid_input": ui[7]
}

settings = {
    "-1": "in_dev_warning",
    "-2": "auto_install"
}

def run():
    print("settings")
    user_input = ""
    in_settings = True
    while in_settings:
        user_input = input(ui["prompt"])
        if user_input in ["--reset", "-r"]:
            print("reset settings")
        elif user_input in ["--save", "-s"]:
            in_settings = False
        elif user_input in settings:
            options[settings[user_input]] = not(options[settings[user_input]])
            print(settings[user_input])
        else:
            print(ui["invalid_input"])

    with open(os.path.join(file_path, "options.json"), "w") as options_file:
        json.dump(options, options_file, separators=(",", ":"))
        print("saved & exited")