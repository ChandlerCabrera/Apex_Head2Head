import requests
import json

key = "8cae2b69-e13a-4bb3-b09e-88111df5e954"
base_url = "https://public-api.tracker.gg/v2/apex/standard/profile/"
headers = {"TRN-API-Key":key}
endpoint = ""
response = ""

platform = "origin"
ign = "Verumictus"

endpoint = f"{platform}/{ign}"



def response_to_json(resp):
    with open("output.json", "w", encoding = "utf=8") as file:
        file.write(resp)
    


def request_player_info():
    response = requests.get(base_url+endpoint, headers = headers)
    print(response.status_code)
     
    data = json.loads(response.text)

    print(data["data"]["platformInfo"]["platformUserId"])
    #print(json.dumps(data, indent = 4))




    #print(response.text)
    #response_to_json(response.text)
    #data = json.loads(response)


print(base_url + endpoint)

request_player_info()


    
    

