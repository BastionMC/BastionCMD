# This file's main purpose is to make stuff look good, it's not very readable.
# Like there's no order at all lol.

from colorama import *

max_action_display_name_length = 32
additional_action_display_name_length = 70

def format_display(display_key, longer=False):
    max_display_length = max_action_display_name_length
    additional_display_length = additional_action_display_name_length

    if len(display_key) > max_display_length and not longer:
        cropped_key = display_key[:max_display_length - 3] + "..."
    elif len(display_key) > additional_display_length:
        cropped_key = display_key[:additional_display_length - 3] + "..."
    else:
        cropped_key = display_key
    
    space_characters = max_action_display_name_length - len(cropped_key)
    display_output = "- " + cropped_key + " " * space_characters
    return display_output

def format_associated_file(display_key, longer=False):
    max_display_length = max_action_display_name_length
    additional_display_length = additional_action_display_name_length

    if len(display_key) > max_display_length and not longer:
        cropped_key = display_key[:max_display_length - 3] + "..."
    elif len(display_key) > additional_display_length:
        cropped_key = display_key[:additional_display_length - 3] + "..."
    else:
        cropped_key = display_key
    
    space_characters = max_action_display_name_length - len(cropped_key)
    associated_file_output = "  " + cropped_key + " " * space_characters
    return Fore.BLACK + Style.BRIGHT + associated_file_output + Style.RESET_ALL

def format_command(display_key, longer=False):
    max_display_length = max_action_display_name_length
    additional_display_length = additional_action_display_name_length

    if len(display_key) > max_display_length and not longer:
        cropped_key = display_key[:max_display_length - 3] + "..."
    elif len(display_key) > additional_display_length:
        cropped_key = display_key[:additional_display_length - 3] + "..."
    else:
        cropped_key = display_key
    
    space_characters = max_action_display_name_length - len(cropped_key)
    associated_file_output = "> " + cropped_key + " " * space_characters
    return Fore.BLACK + Style.BRIGHT + associated_file_output + Style.RESET_ALL

def split_string(text, at):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= at:
            if current_line: current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    for i in range(0, len(lines)):
        if i != 0:
            lines[i] = " " + lines[i]

    return lines

def format_description(display_key):
    additional_display_length = additional_action_display_name_length

    lines = split_string(display_key, additional_display_length)
    formatted_display_key = "\n".join(lines)

    return formatted_display_key

def is_even(int):
    if (int % 2) == 0:
        return True
    else:
        return False
     
def actions_compact(actions):
    for i in range(0, len(actions), 2):
        first_display_name = format_display(actions[i]["display"])
        first_associated_file = format_associated_file(actions[i]["associated_file"])
        
        second_display_name = ""
        second_associated_file = ""

        if i + 1 < len(actions):
            second_display_name = format_display(actions[i + 1]["display"])
            second_associated_file = format_associated_file(actions[i + 1]["associated_file"])

        print(" " + first_display_name + "   " + second_display_name)
        print(" " + first_associated_file + "   " + second_associated_file + "\n")

def actions_full(actions):
    print("")
    for i in range(0, len(actions)):
        display_name = format_display(actions[i]["display"], False)
        associated_file = format_associated_file(actions[i]["associated_file"])
        description = format_description(actions[i]["description"])

        split()
        print(" " + display_name)
        print(" " + associated_file + "\n")
        print(" " + description + "\n")

def commands_full(commands):
    print("")
    for i in range(0, len(commands)):
        command = format_command(commands[i]["command"])
        description = format_description(commands[i]["description"])

        split()
        print(" " + command + "\n")
        print(" " + description + "\n")

def split():
    print(Fore.WHITE + "-------------------------------------------------------------------------\n" + Style.RESET_ALL)

def introduction(actions):
    print(Back.WHITE + Fore.BLACK + "     Welcome to the BastionCMD tool! Type an action ID to continue.      " + Back.BLACK + "." + Style.RESET_ALL + "\n")
    actions_compact(actions)
    split()
    print(Fore.BLACK + Style.BRIGHT + " full - Show a full list of actions without cropped names and\n        descriptions for each option\n" + Style.RESET_ALL)
    print(Fore.BLACK + Style.BRIGHT + " cmds - Show a full list of all navigation commands\n" + Style.RESET_ALL)
    print(Fore.BLACK + Style.BRIGHT + " exit - Exit BastionCMD\n" + Style.RESET_ALL)
    split()

def scroll():
    print(Fore.BLACK + Style.BRIGHT + "                              (Scroll up)" + Style.RESET_ALL)

def stop_scroll():
    print(Fore.BLACK + Style.BRIGHT + "                            (Stop scrolling)" + Style.RESET_ALL)

# Remove this once development is complete
def in_development():
    print(Back.YELLOW + Fore.BLACK + "             Disclaimer: BastionCMD is still in development!             " + Back.BLACK + "." + Style.RESET_ALL + "\n")
    print(" " + "\n".join(split_string("This tool is still in development! Some actions are still placeholders and not fully finished, and you might experience some bugs while using it. Please report any new issues and typos that you find, which aren't yet mentioned as an issue on GitHub, but only if you are on the newest version, thanks!\n- The Bastion Team\n", additional_action_display_name_length)) + "\n")
# ^^^
def debug_enabled():
    print("\n" + Fore.YELLOW + " ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀   Debug mode enabled!   ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀ " + Style.RESET_ALL + "\n")
    print(" " + "\n".join(split_string("Debug mode is experimental and might not work as intended, mainly JSON files not being displayed properly. It is not the optimal way to use BastionCMD. If you'd like to disabled debug mode, just type \"debug\" again.\n", additional_action_display_name_length)) + "\n")

def debug_disabled():
    print("\n" + Fore.YELLOW + " ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀   Debug mode disabled!  ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀ ▄█▀ " + Style.RESET_ALL + "\n")

def clear_enabled():
    print("\n" + Back.WHITE + Fore.BLACK + "                        Screen clearing enabled!                         " + Style.RESET_ALL + "\n")
def clear_disabled():
    print("\n" + Back.WHITE + Fore.BLACK + "                       Screen clearing disabled!                         " + Style.RESET_ALL + "\n")
def shortcut_run():
    print("\n" + Back.WHITE + Fore.BLACK + "                         You just ran a shortcut!                        " + Back.BLACK + "." + Style.RESET_ALL + "\n")
    print(" " + "\n".join(split_string("Shorcuts allow you to easily execute single actions with one command, and it allows you to automate them! You will return to the command prompt after this shortcut is done running.\n", additional_action_display_name_length)))