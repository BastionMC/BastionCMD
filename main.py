import cticf
import server, update, actions

import os, sys
from pathlib import Path

import renput

file_path = Path(sys.argv[0]).parent.absolute()

ui_files = []
ui_file_names = [ # If you added a new .cticf file, add it's name here
    "menu",
    "settings"
]
ui = {}

for file in os.listdir(file_path):
    if file.endswith(".cticf"):
        ui_files.append(os.path.join(file_path, file))

for ui_file in ui_files:
    for ui_file_name in ui_file_names:
        if ui_file_name in ui_file: ui[ui_file_name] = cticf.rfile(ui_file)

ui["divider"] = ui["menu"][0]
ui["title"] = ui["menu"][5]
ui["requirements"] = {
    "banner": ui["menu"][13],
    "internet": ui["menu"][11],
    "windows": ui["menu"][8],
    "linux": ui["menu"][7]
}

ui["dialogs"] = {
    "in_development": ui["menu"][16], # TODO: Remove once project is complete (DONT FORGET TO UPDATE INDEX)
    "no_connection": ui["menu"][4]
}

ui["commands"] = ui["menu"][14]
ui["needs_update"] = ui["menu"][15]

def intro():
    print("\n" + ui["title"] + "\n\n" + ui["requirements"]["banner"] + "\n\n" + ui["divider"])
    
    if not(server.needs_update()[0]):
        print("\n" + cticf.inserts(ui["needs_update"], server.needs_update()[1]) + "\n\n" + ui["divider"])
    
    print("\n" + ui["commands"] + "\n\n" + ui["divider"])

if not(server.connection()): print("\n" + ui["dialogs"]["no_connection"])
print("\n" + ui["dialogs"]["in_development"]) # TODO: Remove once project is complete

intro()