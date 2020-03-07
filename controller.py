from model import Player
import requests
import json

key = "8cae2b69-e13a-4bb3-b09e-88111df5e954"
base_url = "https://public-api.tracker.gg/v2/apex/standard/profile/"
headers = {"TRN-API-Key":key}
endpoint = ""
response = ""


def response_to_json(resp):
    with open("output.json", "w", encoding = "utf=8") as file:
        file.write(resp)


def api_request(endpoint):
    response = requests.get(base_url + endpoint, headers = headers)
    return json.loads(response.text)

