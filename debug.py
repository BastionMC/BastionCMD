# This is for debug's mode dictionary syntax highlighting.
# It's not for real-time highlighting, as it's performance isn't the best...

from colorama import *

def get_dictionary_syntax_highlighting(dictionary):
    in_string = False
    bracket_level = 0
    result = ""
    escape = False
    string_color = False

    for char in dictionary:
        if escape and in_string:
            string_color = True
            escape = False

        if char == "\\":
            escape = True

        if char == "\"" and not escape:
            in_string = not in_string

        if in_string or char == "\"":
            result += Fore.BLACK + Style.BRIGHT + char + Style.RESET_ALL
        elif string_color:
            string_color = False
            result += Fore.BLACK + Style.BRIGHT + char + Style.RESET_ALL
            in_string = True
        elif char in "{[(":
            bracket_level += 1
            if bracket_level % 3 == 1: result += Fore.RED + Style.BRIGHT + char + Style.RESET_ALL
            elif bracket_level % 3 == 2: result += Fore.GREEN + Style.BRIGHT + char + Style.RESET_ALL
            elif bracket_level % 3 == 0: result += Fore.BLUE + Style.BRIGHT + char + Style.RESET_ALL
        elif char in "}])":
            if bracket_level % 3 == 1: result += Fore.RED + Style.BRIGHT + char + Style.RESET_ALL
            elif bracket_level % 3 == 2: result += Fore.GREEN + Style.BRIGHT + char + Style.RESET_ALL
            elif bracket_level % 3 == 0: result += Fore.BLUE + Style.BRIGHT + char + Style.RESET_ALL
            bracket_level -= 1
        elif char in "0123456789":
            result += Fore.CYAN + Style.BRIGHT + char + Style.RESET_ALL
        elif char in ":.,-+*/":
            result += char
        else:
            result += Fore.BLACK + Style.BRIGHT + char + Style.RESET_ALL
    return result