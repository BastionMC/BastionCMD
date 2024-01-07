import json

with open("options.json", "r") as file:
    options = json.load(file)

import requests, traceback, crash_handler

# If you're hosting the API yourself, change this to your server.
server_url = "https://bastionmc.github.io/api/cmd/"
# Use "dev" for development, as dev versions will always say
# they need an update. The "update" command refuses to replace
# a version of BastionCMD that is labled as "dev", however the
# rest of the command still works as normal.
version = "dev"

def connection():
    try:
        requests.get(server_url + "connection.txt", timeout=5)
        return True
    except requests.ConnectionError:
        return False
        
def get_file(file: str):
    req = requests.get(server_url + file)
    if req.status_code == 200:
        return json.loads(req.text)
    else:
        return req.status_code
        
def get_version():
    return get_file("version.json")

def needs_update():
    version_json = get_version()
    if version in version_json["valid"] and not(version == version_json["latest"]) and not(version == options["skipped_update"]):
        return [True, version_json["latest"]]
    else:
        return [False, version_json["latest"]]