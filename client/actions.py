from pathlib import Path
import os, sys, json
import formatting

file_path = Path(sys.argv[0]).parent.absolute()

actions = []

def process_action(action: str):
    with open(os.path.join(file_path, "actions", action, "action.json")) as action_json:
        action_info = json.loads(action_json.read())
        actions.append(action_info)
        action_info["path"] = action
        return action_info

for action in os.listdir(os.path.join(file_path, "actions/")):
    if "." in action: continue
    process_action(action)

def showcase_actions():
    showcased_actions = []
    planned_showcase_actions = actions[:6]

    for action in planned_showcase_actions:
        showcase_action = {
            "description": formatting.split_up(action["description"], 27),
            "path": formatting.fill_space(formatting.cut_off(action["path"], 23), 24),
            "windows": action["windows"],
            "linux": action["linux"],
            "needs_connection": action["needs_connection"],
        }

        for i in range(0, len(showcase_action["description"])):
            showcase_action["description"][i] = formatting.fill_space(showcase_action["description"][i], 27)

        showcased_actions.append(showcase_action)

    showcased_actions.sort(key=lambda x: len(x["description"]), reverse=True)

    return showcased_actions