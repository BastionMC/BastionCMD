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
    "invalid_input": ui[6],

    "title": ui[2],

    "on": ui[3],
    "off": ui[4],

    "commands": ui[5],
    "saved": ui[7],
    "reset": ui[8]
}

settings = {
    "1": "in_dev_warning",
    "2": "auto_install"
}
settings_display = {
    "in_dev_warning": "Disable In-dev Splash Message",
    "auto_install": "Automatically install updates"
}
settings_display = {key:formatting.fill_space(value, 46) for (key,value) in settings_display.items()}

def print_settings():
    print("\n" + ui["title"] + "\n")

    for setting in settings:
        if options[settings[setting]]:
            print(cticf.inserts(ui["off"], settings_display[settings[setting]], setting))
        else:
            print(cticf.inserts(ui["on"], settings_display[settings[setting]], setting))

    print("\n" + ui["commands"] + "\n\n" + ui["divider"])

def run():
    user_input = ""
    in_settings = True
    pre_promt = ""

    while in_settings:
        formatting.clear_screen()
        print_settings()
        print(pre_promt)
        pre_promt = ""

        user_input = input(ui["prompt"])
        if user_input in ["--reset", "-r"]:
            options["skipped_update"] = None
            options["in_dev_warning"] = True
            options["auto_install"] = False

            pre_promt = "\n" + ui["reset"] + "\n"
        elif user_input in ["--save", "-s"]:
            in_settings = False
        elif user_input in settings:
            options[settings[user_input]] = not(options[settings[user_input]])
        else:
            pre_promt = "\n" + ui["invalid_input"] + "\n"

    with open(os.path.join(file_path, "options.json"), "w") as options_file:
        json.dump(options, options_file, separators=(",", ":"))
        print("\n" + ui["saved"] + "\n")