# Console Text Indexing & Coloring Format
#      Copyright (c) Bastion 2024
# CTICF is licensed under the MIT license.

import re, os
from colorama import *

if os.name == "nt": just_fix_windows_console()

def get_color(color: str):
    ground, brightness = {
        "f": Fore,
        "b": Back
    }, {
        "d": Style.DIM,
        "n": Style.NORMAL,
        "b": Style.BRIGHT
    }
    ground, brightness = ground[color[2]], brightness[color[1]]
    colors = {
        "r": ground.RED,
        "g": ground.GREEN,
        "y": ground.YELLOW,
        "b": ground.BLUE,
        "m": ground.MAGENTA,
        "c": ground.CYAN,
        "w": ground.WHITE,
        "0": ground.BLACK
    }
    color = colors[color[0]]

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