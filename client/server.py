import requests, json

# If you're hosting the API yourself, change this to your server.
server_url = "https://bastionmc.github.io/api/cmd/"
version = "1.0"

def connection():
    try:
        requests.get(server_url, timeout=5)
        return True
    except requests.ConnectionError:
        return False
        
def get_file(file):
    req = requests.get(server_url + file)
    if req.status_code == 200:
        return json.loads(req.text)
    else:
        return req.status_code
        
def get_version():
    return get_file("version.json")

def needs_update():
    global version

    version_json = get_version()
    if version in version_json["valid"]:
        if not(version == version_json["latest"]):
            return [True, version_json["latest"]]
        else: return [False, version_json["latest"]]
    else: return [False, version_json["latest"]]