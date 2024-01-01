# This project uses snake_case instead of lowerCamelCase and CamelCase, please
# keep this consistent across all files of this project, thanks.

from os import system as run_command
from json import loads as convert_json_to_dictionary
from colorama import *
from formatting import *
from debug import *
from renput import *

just_fix_windows_console() # Just fixes the windows console, from colorama.
run_command("color 07") # Set colors to default.

with open("actions.json", "r") as actions_file:
    actions_file_content = actions_file.read()
    actions = convert_json_to_dictionary(actions_file_content)["actions"]
    actions_file.close()

with open("commands.json", "r") as commands_file:
    commands_file_content = commands_file.read()
    commands = convert_json_to_dictionary(commands_file_content)["commands"]
    commands_file.close()

try:
    if sys.argv[1] != "":
        shortcut_run()
        running = False
        run_command("start " + sys.argv[1])
    else:
        running = True
except:
    running = True
debug = False
clear = False

if running:
    print("")
    # Remove this once development is complete
    in_development()
    # ^^^
    introduction(actions)

associated_files = []
for action in actions:
    associated_files.append(action["associated_file"])

possible_inputs = ["exit", "full", "intro", "cmds", "clear"] + associated_files

while running:

    to_run = input(Fore.BLACK + Style.BRIGHT + "> " + Style.RESET_ALL, possible_inputs)
    
    if clear:
        run_command("cls")

    match to_run:
        case ("exit", "esc", "escape", "close", "quit"):
            running = False
        case ("full", "all", "actions", "all_actions", "full_actions"):
            if not debug:
                stop_scroll()
                actions_full(actions)
                split()
                scroll()
            else:
                print(get_dictionary_syntax_highlighting(actions_file_content))
        case ("intro", "introduction", "opening", "main_menu", "home", "back", "main"):
            if not debug:
                print("")
                split()
                introduction(actions)
            else:
                print(get_dictionary_syntax_highlighting(actions_file_content))
        case ("cmds", "commands", "nav", "navigation", "navigation_commands", "all_commands", "full_commands"):
            if not debug:
                stop_scroll()
                commands_full(commands)
                split()
                scroll()
            else:
                print(get_dictionary_syntax_highlighting(commands_file_content))
        case ("debug", "dbug", "bug", "raw", "json", "view_raw", "view_json", "enable_debug", "disable_debug", "enable_dbug", "disable_dbug"):
            debug = not debug
            if debug:
                debug_disabled()
            else:
                debug_enabled()
        case ("clear", "clear_screen", "screen_clearing", "enable_clear", "enable_clear_screen", "enable_screen_clearing", "disable_clear", "disable_clear_screen", "disable_screen_clearing"):
            clear = not clear
            if clear:
                clear_disabled()
            else:
                clear_enabled()
        case associated_files_:
            print("thats gay tho")