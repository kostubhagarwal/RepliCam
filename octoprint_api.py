import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

def send_print(filename: str):
    url = os.environ.get("OCTOPRINT_URL") + "/api/files"
    api_key = os.environ.get("OCTOPRINT_KEY")
    resp = requests.post(url, headers={
        "X-Api-Key": api_key,
        "Content-Type": "multipart/form-data",
        "file": open(filename, "rb").read()
    })

    print(json.loads(resp))

if __name__ == "__main__":
    send_print("test.gcode")


