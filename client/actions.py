from pathlib import Path
import os, sys, json
import formatting

file_path = Path(sys.argv[0]).parent.absolute()

def crop_action_path(path):
    if len(path) > 27:
        cropped_path = path[:23 - 3] + "..."
    else: cropped_path = path

def process_action(action):
    with open(os.path.join(action, "action.json")) as action_json:
        action_info = json.loads(action_json.read())

for action in os.listdir(os.path.join(file_path, "actions/")):
    process_action(action)