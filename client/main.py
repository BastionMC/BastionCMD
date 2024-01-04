import cticf
import server, update, action, formatting

import os, sys
from pathlib import Path

import traceback, crash_handler

file_path = Path(sys.argv[0]).parent.absolute()

ui_files = []
ui_file_names = [ # If you added a new .cticf file, add it's name here
    "menu",
    "settings"
]
ui = {}


try:
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
        "windows": ui["menu"][9],
        "linux": ui["menu"][10]
    }

    ui["errors"] = {
        "normal": ui["menu"][2],
        "fatal": ui["menu"][3]
    }

    ui["dialogs"] = {
        "in_development": ui["menu"][20], # TODO: Remove once project is complete (DONT FORGET TO UPDATE INDEX)
        "no_connection": ui["menu"][4]
    }

    ui["commands"] = ui["menu"][14]
    ui["needs_update"] = ui["menu"][15]

    ui["action_squares"] = [
        ui["menu"][8],
        ui["menu"][7],
        ui["menu"][6]
    ]
    ui["actions_abreviated"] = ui["menu"][12]

    ui["action_segment_error"] = ui["menu"][16]
    ui["no_actions"] = ui["menu"][17]

    ui["prompt"] = ui["menu"][1]
    ui["input_error"] = {
        "command": ui["menu"][18],
        "action": ui["menu"][19]
    }

except Exception as e:
    if type(e) == IndexError:
        crash_handler.fatal_error(traceback.format_exc(), reason=formatting.split_up("Error Note: There was an IndexError whilst loading the UI. Either a developer forgot to update the index, or a user messed with the files. Was that you?", 64))
    elif type(e) == KeyError:
        crash_handler.fatal_error(traceback.format_exc(), reason=formatting.split_up("Error Note: Did you seriously delete a .CTICF file? Those are kinda important, y'know. Or maybe you didn't, I'm asuming this because I got a KeyError.", 64))
    else:
        crash_handler.fatal_error(traceback.format_exc())

def intro_actions():
    try:
        showcase_actions = action.showcase_actions()
    except Exception as e:
        crash_handler.fatal_error(traceback.format_exc())

    action_squares = [showcase_actions[i:i+2] for i in range(0,len(showcase_actions),2)]

    print("")

    failed_to_load = False
    failed_to_load_error = ""

    try:
        for segment in action_squares:
            height = max(len(segment[0]["description"]), len(segment[1]["description"]))

            more_info = []

            for action_box in segment:
                while len(action_box["description"]) < height:
                    action_box["description"].append(27 * " ")

                more_info.append(action_box["path"])
                
                requirements_text = ""

                # TODO: Get better at coding.

                if action_box["windows"]: requirements_text += "W"
                if action_box["linux"]: requirements_text += "L"
                if action_box["needs_connection"]: requirements_text += "!"

                requirements_text = formatting.fill_space(requirements_text, 3, reverse=True)

                requirements_text = requirements_text.replace(
                "W", ui["requirements"]["windows"]).replace(
                "L", ui["requirements"]["linux"]).replace(
                "!", ui["requirements"]["internet"])

                # TODO: Get better at coding end.

                more_info.append(requirements_text)

            formatted_description = formatting.line_for_line(segment[0]["description"], segment[1]["description"])

            print(cticf.inserts(
                ui["action_squares"][height-1],
                *formatted_description,
                *more_info
            ))
    except Exception as e:
        if type(e) == IndexError:
            failed_to_load = True
            failed_to_load_error = traceback.format_exc()
            print(ui["action_segment_error"])
        else:
            crash_handler.error(traceback.format_exc())

    if failed_to_load:
        crash_handler.error(failed_to_load_error, reason=formatting.split_up("Error Note: Seems like there was an IndexError. This is probably because there aren't enough action. (An amount of 2, 4, or 6 is required for the client to run flawlessly. 1, 3, or 5 won't work.) Don't worry, the client can still run, you'll just be seeing this error every time. You can disable non-fatal errors in the settings.", 64))

    if len(action.actions) > 6:
        print("\n" + cticf.inserts(ui["actions_abreviated"], len(action.actions) - 6))

    if len(action.actions) == 0:
        print(ui["no_actions"])

needs_update = False

def intro():
    print("\n" + ui["title"])

    intro_actions()

    print("\n" + ui["requirements"]["banner"] + "\n\n" + ui["divider"])
    
    if needs_update:
        print("\n" + cticf.inserts(ui["needs_update"], server.needs_update()[1]) + "\n\n" + ui["divider"])
    
    print("\n" + ui["commands"] + "\n\n" + ui["divider"] + "\n")

input_actions = []
input_commands = [
    "--settings",
    "--actions",
    "--help",
    "--discord",
    "--github"
]
input_commands_short = [
    "-s",
    "-a",
    "-h",
    "-d",
    "-g"
]

for input_action in action.actions:
    input_actions.append(input_action["path"])

def input_run(type: str = "action", input_string: str = ""):
    return

def input_main():
    while True:
        user_input = input(ui["prompt"])

        if user_input.startswith("-"):
            
            if user_input.startswith("--") and user_input in input_commands:
                input_run(type = "command", input_string = user_input)
            elif user_input in input_commands_short:
                for command in input_commands:
                    if user_input in command:
                        input_run(type = "command", input_string = command)
            else:
                print(ui["input_error"]["command"])
        elif user_input in input_actions:
            input_run(type = "action")
        elif user_input == "cls":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            print(ui["input_error"]["action"])

if server.connection() and server.needs_update()[0]:
    needs_update = True
    input_commands.extend(["--ignore", "--update"])
    input_commands_short.extend(["-i", "-u"])

if not(server.connection()): print("\n" + ui["dialogs"]["no_connection"])
print("\n" + ui["dialogs"]["in_development"]) # TODO: Remove once project is complete

intro()
input_main()