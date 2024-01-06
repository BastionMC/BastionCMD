from pathlib import Path
from importlib import import_module
import os, sys, json, formatting

import traceback, crash_handler

file_path = Path(sys.argv[0]).parent.absolute()

actions = []

def process_action(action: str):
    with open(os.path.join(file_path, "actions", action, "action.json")) as action_json:
        action_info = json.loads(action_json.read())
        actions.append(action_info)
        action_info["path"] = action
        return action_info

for action in os.listdir(os.path.join(file_path, "actions/")):
    try:
        if "." in action: continue
        process_action(action)
    except Exception as e:
        crash_handler.error(traceback.format_exc())


def format_showcase_action(action):
    showcase_action = {
        "description": formatting.split_up(action["description"], 27),
        "path": formatting.fill_space(formatting.cut_off(action["path"], 23), 23),
        "windows": action["windows"],
        "linux": action["linux"],
        "needs_connection": action["needs_connection"],
    }

    for i in range(0, len(showcase_action["description"])):
        showcase_action["description"][i] = formatting.fill_space(showcase_action["description"][i], 27)

    return showcase_action


def showcase_actions():
    showcased_actions = []

    try:
        planned_showcase_actions = actions[:6]

        for action in planned_showcase_actions:
            showcased_actions.append(format_showcase_action(action))

        showcased_actions.sort(key=lambda x: len(x["description"]), reverse=True)

        return showcased_actions
    except Exception as e:
        crash_handler.fatal_error(traceback.format_exc())

def run_action(action: str):
    return