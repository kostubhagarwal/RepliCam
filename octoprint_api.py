import requests
from dotenv import load_dotenv
import os
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

load_dotenv()

def upload_print(filename: str):
    url = os.environ.get("OCTOPRINT_URL") + "/api/files/local"
    api_key = os.environ.get("OCTOPRINT_KEY")
    file = open(filename, 'rb')
    multipart_data = MultipartEncoder({
        'file': (filename, file, 'application/octet-stream')})
    resp = requests.post(url, data=multipart_data, headers={
        "X-Api-Key": api_key,
        "Content-Type": multipart_data.content_type
    })
    print(resp.json())

    print("\nselect")
    url = os.environ.get("OCTOPRINT_URL") + "/api/files/local/" + filename
    resp2 = requests.post(
        url,
        headers={
            "X-Api-Key": api_key,
            "Content-Type": "application/json"
        },
        json=json.dumps({"command": "select"})
    )
    print(resp2.json(), resp2.status_code)


def start_print():
    url = os.environ.get("OCTOPRINT_URL") + "/api/job"
    api_key = os.environ.get("OCTOPRINT_KEY")
    resp = requests.post(
        url, 
        headers={
            "X-Api-Key": api_key,
            "Content-Type": "application/json",
        },
        json=json.dumps({"command": "start"}))
    print(resp.json())

if __name__ == "__main__":
    upload_print("test2.gcode")
    start_print()


