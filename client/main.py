import cticf, server, action, formatting, os, sys, requests, traceback, crash_handler
from pathlib import Path
import feature.settings, feature.actions, feature.help, feature.discord, feature.github, feature.ignore, feature.update

file_path = Path(sys.argv[0]).parent.absolute()
action_amount = len(action.actions)
needs_update, update_version = [False, None], None

with requests.Session() as session:
    needs_update, has_connection = server.needs_update(), server.connection()

input_actions, input_commands, input_commands_short = [], {
    "--settings": feature.settings.run,
    "--actions": feature.actions.run,
    "--help": feature.help.run,
    "--discord": feature.discord.run,
    "--github": feature.github.run
}, {
    "-s": "--settings",
    "-a": "--actions",
    "-h": "--help",
    "-d": "--discord",
    "-g": "--github"
}

try:
    ui = cticf.rfile(os.path.join(file_path, "menu.cticf"))

    ui = {
        "divider": ui[0],
        "title": ui[5],

        "requirements": {
            "banner": ui[13],
            "internet": ui[11],
            "windows": ui[9],
            "linux": ui[10]
        },

        "dialogs": {
            "in_development": ui[21], # TODO: Remove once project is complete (DONT FORGET TO UPDATE INDEX)
            "no_connection": ui[4]
        },

        "commands": ui[14],
        "needs_update": ui[15],

        "action_squares": [
            ui[8],
            ui[7],
            ui[6]
        ],
        "actions_abreviated": ui[12],
        "action_abreviated": ui[20],
        "action_segment_error": ui[16],
        "no_actions": ui[17],

        "prompt": ui[1],
        "input_error": {
            "command": ui[18],
            "action": ui[19]
        }
    }
except Exception as e:
    if type(e) == IndexError:
        crash_handler.fatal_error(traceback.format_exc(), reason=formatting.split_up("Error Note: There was an IndexError whilst loading the UI. Either a developer forgot to update the index, or a user messed with the files. Was that you?", 64))
    elif type(e) == KeyError:
        crash_handler.fatal_error(traceback.format_exc(), reason=formatting.split_up("Error Note: Did you seriously delete a .CTICF file? Those are kinda important, y'know. Or maybe you didn't, I'm asuming this because I got a KeyError.", 64))
    else:
        crash_handler.fatal_error(traceback.format_exc())

def action_square_segment(segment):
    height = max(len(segment[0]["description"]), len(segment[1]["description"]))

    more_info = []

    for action_box in segment:
        while len(action_box["description"]) < height:
            action_box["description"].append(27 * " ")

        more_info.append(action_box["path"])
        
        text = ""

        if action_box["windows"]: text += ui["requirements"]["windows"]
        if action_box["linux"]: text += ui["requirements"]["linux"]
        if action_box["needs_connection"]: text += ui["requirements"]["internet"]

        characters = text.count("W") + text.count("L") + text.count("↓")
        text = (" "*(3 - characters)) + text

        more_info.append(text)

    formatted_description = formatting.line_for_line(segment[0]["description"], segment[1]["description"])

    print(cticf.inserts(
        ui["action_squares"][height-1],
        *formatted_description,
        *more_info
    ))

def intro_actions():
    print("")

    try: showcase_actions = action.showcase_actions()
    except Exception as e:
        crash_handler.fatal_error(traceback.format_exc())

    # Splits actions up into pairs of two.
    action_squares = [showcase_actions[i:i+2] for i in range(0,len(showcase_actions),2)]

    failed_to_load, failed_to_load_error = False, ""

    try:
        for segment in action_squares:
            action_square_segment(segment)
    except Exception as e:
        if type(e) == IndexError:
            failed_to_load, failed_to_load_error = True, traceback.format_exc()
            print(ui["action_segment_error"])
        else:
            crash_handler.error(traceback.format_exc())

    if failed_to_load:
        crash_handler.error(failed_to_load_error, reason=formatting.split_up("Error Note: Seems like there was an IndexError. This is probably because there aren't enough actions. (An amount of 2, 4, or 6 is required for the client to run flawlessly. 1, 3, or 5 won't work.) Don't worry, the client can still run, you'll just be seeing this error every time. You can disable non-fatal errors in the settings.", 64))

    if action_amount == 7:
        print("\n" + cticf.inserts(ui["action_abreviated"], 1))
    elif action_amount > 6:
        print("\n" + cticf.inserts(ui["actions_abreviated"], action_amount - 6))
    elif action_amount == 0:
        print(ui["no_actions"])

def intro():
    print("\n" + ui["title"])

    intro_actions()

    print("\n" + ui["requirements"]["banner"] + "\n\n" + ui["divider"])
    
    if needs_update[0]:
        print("\n" + cticf.inserts(ui["needs_update"], needs_update[1]) + "\n\n" + ui["divider"])
    
    print("\n" + ui["commands"] + "\n\n" + ui["divider"] + "\n")

def input_run(type: str="action", input_string: str=""):
    match type:
        case "action":
            action.run_action(input_string)
        case "command":
            input_commands[input_string]()

def input_command(user_input):
    if user_input in input_commands:
        input_run(type="command", input_string=user_input)
    elif user_input in input_commands_short:
        input_run(type="command", input_string=input_commands_short[user_input])
    else:
        print(ui["input_error"]["command"])

def input_main():
    while True:
        user_input = input(ui["prompt"])

        if user_input.startswith("-"):
            input_command(user_input)
        elif user_input in input_actions:
            input_run(type="action", input_string=user_input)
        elif user_input in ["cls", "clear"]:
            formatting.clear_screen()
            print("\n" + ui["commands"] + "\n\n" + ui["divider"] + "\n")
        else:
            print(ui["input_error"]["action"])


for input_action in action.actions:
    input_actions.append(input_action["path"])

if has_connection and needs_update[0]:
    input_commands["--ignore"], input_commands["--update"] = feature.ignore.run, feature.update.run
    input_commands_short["-i"], input_commands_short["-u"] = "--ignore", "--update"
    update_version = needs_update[1]
elif not(has_connection):
    print("\n" + ui["dialogs"]["no_connection"])

print("\n" + ui["dialogs"]["in_development"]) # TODO: Remove once project is complete

try:
    intro()
    input_main()
except Exception as e:
    crash_handler.fatal_error(traceback.format_exc())