import cticf
import server, update, actions, formatting

import os, sys
from pathlib import Path

import renput
if os.name == "nt": input = renput.input

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

ui["action_squares"] = [
    ui["menu"][8],
    ui["menu"][7],
    ui["menu"][6]
]

def intro_actions():
    showcase_actions = actions.showcase_actions()
    action_squares = [showcase_actions[i:i+2] for i in range(0,len(showcase_actions),2)]

    for segment in action_squares:
        height = max(len(segment[0]["description"]), len(segment[1]["description"]))

        for action in segment:
            while len(action["description"]) < height:
                action["description"].append(27 * " ")

        formatted_description = formatting.line_for_line(segment[0]["description"], segment[1]["description"])

        print(cticf.inserts(
            ui["action_squares"][height-1],
            *formatted_description
        ))

def intro():
    print("\n" + ui["title"])

    intro_actions()

    print("\n" + ui["requirements"]["banner"] + "\n\n" + ui["divider"])
    
    if server.connection() and server.needs_update()[0]:
        print("\n" + cticf.inserts(ui["needs_update"], server.needs_update()[1]) + "\n\n" + ui["divider"])
    
    print("\n" + ui["commands"] + "\n\n" + ui["divider"])

if not(server.connection()): print("\n" + ui["dialogs"]["no_connection"])
print("\n" + ui["dialogs"]["in_development"]) # TODO: Remove once project is complete

intro()