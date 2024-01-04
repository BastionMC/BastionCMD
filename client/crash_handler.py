import cticf

import os, sys
from pathlib import Path

file_path = Path(sys.argv[0]).parent.absolute()

ui_files = []
ui_file_names = [
    "menu"
]
ui = {}

import traceback, formatting

def error(error: str = "No further information.", reason: list = []):
    final_message = error

    for line in reason:
        final_message += "\n" + line

    if len(reason) > 0:
        final_message += "\n "

    print("\n" + cticf.inserts(ui["errors"]["normal"], "\n" + final_message) + "\n")

def fatal_error(error: str = "No further information.", reason: list = []):
    final_message = error

    for line in reason:
        final_message += "\n" + line

    if len(reason) > 0:
        final_message += "\n "

    print("\n" + cticf.inserts(ui["errors"]["fatal"], "\n" + final_message) + "\n")
    exit()


try:
    for file in os.listdir(file_path):
        if file.endswith(".cticf"):
            ui_files.append(os.path.join(file_path, file))

    for ui_file in ui_files:
        for ui_file_name in ui_file_names:
            if ui_file_name in ui_file: ui[ui_file_name] = cticf.rfile(ui_file)

    ui["errors"] = {
        "normal": ui["menu"][2],
        "fatal": ui["menu"][3]
    }
except Exception as e:
    if type(e) == IndexError:
        try:
            fatal_error(traceback.format_exc(), reason=formatting.split_up("Error Note: There was an IndexError whilst loading the UI. Either a developer forgot to update the index, or a user messed with the files. Was that you?", 64))
        except:
            for line in formatting.split_up("You know the error is bad, when the error message has an error... Please put the .CTICF file back in it's place. They are kinda like Lego Island's .SI files. If you know what those are, you probably already know what the CTICF file controls. Yea. Put it back.", 64):
                print(line)
            exit()
    elif type(e) == KeyError:
        try:
            fatal_error(traceback.format_exc(), reason=formatting.split_up("Error Note: Did you seriously delete a .CTICF file? Those are kinda important, y'know. Or maybe you didn't, I'm asuming this because I got a KeyError.", 64))
        except:
            for line in formatting.split_up("You know the error is bad, when the error message has an error... Please put the .CTICF file back in it's place. They are kinda like Lego Island's .SI files. If you know what those are, you probably already know what the CTICF file controls. Yea. Put it back.", 64):
                print(line)
            exit()
    else:
        fatal_error(traceback.format_exc())