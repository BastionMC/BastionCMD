def fill_space(string: str, length: int):
    if len(string) < length:
        remaining_chars = length - len(string)
        return string + " " * remaining_chars
    else: return string

def cut_off(string: str, length: int):
    if len(string) > length:
        return string[:length - 3] + "..."
    else: return string

def split_up(string: str, length: int):
    words = string.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= length:
            if current_line: current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    for i in range(0, len(lines)):
        if i != 0: lines[i] = lines[i]

    return lines

def line_for_line(list1: list, list2: list):
    final = []

    for i in range(0, len(list1)):
        final.append(list1[i])
        final.append(list2[i])

    return final