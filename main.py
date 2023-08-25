# This project uses snake_case instead of lowerCamelCase and CamelCase, please
# keep this consistent across all files of this project, thanks.

from os import system as run_command
from json import loads as convert_json_to_dictionary
from colorama import *
from formatting import *
from debug import *

just_fix_windows_console() # Just fixes the windows console, from colorama.

max_action_display_name_length = 32

with open("actions.json", "r") as actions_file:
    actions_file_content = actions_file.read()
    actions = convert_json_to_dictionary(actions_file_content)["actions"]
    actions_file.close()

with open("commands.json", "r") as commands_file:
    commands_file_content = commands_file.read()
    commands = convert_json_to_dictionary(commands_file_content)["commands"]
    commands_file.close()

print("")
# Remove this once development is complete
in_development()
# ^^^
introduction(actions)

running = True
debug = False
clear = False

associated_files = []
for action in actions:
    associated_files.append(action["associated_file"])

possible_inputs = ["exit", "full", "intro", "cmds", "clear"].append(associated_files)

while running:
    to_run = input(Fore.BLACK + Style.BRIGHT + "> " + Style.RESET_ALL)

    if clear:
        run_command("cls")

    if to_run in ["exit", "esc", "escape", "close", "quit"]:
        running = False

    elif to_run in ["full", "all", "actions", "all_actions", "full_actions"]:
        if not debug:
            stop_scroll()
            actions_full(actions)
            split()
            scroll()
        else:
            print(get_dictionary_syntax_highlighting(actions_file_content))

    elif to_run in ["intro", "introduction", "opening", "main_menu", "home", "back", "main"]:
        if not debug:
            print("")
            split()
            introduction(actions)
        else:
            print(get_dictionary_syntax_highlighting(actions_file_content))

    elif to_run in ["cmds", "commands", "nav", "navigation", "navigation_commands", "all_commands", "full_commands"]:
        if not debug:
            stop_scroll()
            commands_full(commands)
            split()
            scroll()
        else:
            print(get_dictionary_syntax_highlighting(commands_file_content))

    elif to_run in ["debug", "dbug", "bug", "raw", "json", "view_raw", "view_json", "enable_debug", "disable_debug", "enable_dbug", "disable_dbug"]:
        if debug:
            debug = False
            debug_disabled()
        else:
            debug = True
            debug_enabled()
    elif not to_run in ["clear", "clear_screen", "screen_clearing", "enable_clear", "enable_clear_screen", "enable_screen_clearing", "disable_clear", "disable_clear_screen", "disable_screen_clearing"]:
        run_command(to_run)

    if to_run in ["clear", "clear_screen", "screen_clearing", "enable_clear", "enable_clear_screen", "enable_screen_clearing", "disable_clear", "disable_clear_screen", "disable_screen_clearing"]:
        if clear :
            clear = False
            clear_disabled()
        else:
            clear = True
            clear_enabled()