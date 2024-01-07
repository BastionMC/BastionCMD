import cticf, sys, os, webbrowser
from pathlib import Path
file_path = Path(sys.argv[0]).parent.absolute()

ui = cticf.rfile(os.path.join(file_path, "feature/discord.cticf"))
ui = {
    "divider": ui[0],
    "text": ui[1]
}

def run():
    print("\n" + ui["divider"] + "\n\n" + ui["text"] + "\n\n" + ui["divider"] + "\n")
    try:
        webbrowser.open_new_tab("https://www.discord.gg/KvZJGqMEhU")
    except:
        return