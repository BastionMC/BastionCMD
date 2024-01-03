def fill_space(string, length, fill=" "):
    return f"{string[:length]:<{fill}{length}}"

def cut_off(string, length):
    if len(string) > length:
        return string[:length - 3] + "..."
    else: return string

def split_up(string, length):
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

    if not(current_line): return string

    for i in range(0, len(lines)):
        if i != 0: lines[i] = lines[i]

    return lines