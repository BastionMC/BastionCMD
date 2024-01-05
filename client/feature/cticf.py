# Console Text Indexing & Coloring Format
#      Copyright (c) Bastion 2024
# CTICF is licensed under the MIT license.

import re
from colorama import *

just_fix_windows_console()
    
def get_color(color: str):
    ground = color[2]
    match ground:
        case "f": ground = Fore
        case "b": ground = Back
        case _: ground = Fore
    brightness = color[1]
    match brightness:
        case "d": brightness = Style.DIM
        case "n": brightness = Style.NORMAL
        case "b": brightness = Style.BRIGHT
        case _: brightness = Style.NORMAL
    color = color[0]
    match color:
        case "r": color = ground.RED
        case "g": color = ground.GREEN
        case "y": color = ground.YELLOW
        case "b": color = ground.BLUE
        case "m": color = ground.MAGENTA
        case "c": color = ground.CYAN
        case "w": color = ground.WHITE
        case "0": color = ground.BLACK
        case _: color = ground.WHITE

    return color + brightness

def scolor(string: str):
    pattern = r"§§(\w{3})"
    return re.sub(pattern, lambda match: get_color(match.group(1)), string)

def rfile(path: str):
    with open(path, "r", encoding="utf-8") as cticf_f: cticf_c = cticf_f.read(); cticf_f.close()
    cticf_c = cticf_c.split("#\n")[-1]
    cticf_s = cticf_c.split("$§")
    final = []
    for string in cticf_s:
        string = string.strip().replace("§$", Style.RESET_ALL)
        string = scolor(string)
        final.append(string)
    return final
        
def inserts(text: str, *strings):
    for string in strings:
        text = text.replace("$$", str(string), 1)
    return text