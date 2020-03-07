import requests
import json
import controller as c

key = "8cae2b69-e13a-4bb3-b09e-88111df5e954"
base_url = "https://public-api.tracker.gg/v2/apex/standard/profile/"
headers = {"TRN-API-Key":key}
endpoint = ""
response = ""

class Player(object):
    def __init__(self, platform, ign):
        self.ign = ign
        self.platform = platform
        self.endpoint = f"{self.platform}/{self.ign}"
        self.kd = 0
        
    def get_main_legend(self):
        data = c.api_request(self.endpoint)
        lifetime_kills = data["data"]["segments"][0]["stats"]["kills"]["value"]

        legend_data = c.api_request(self.endpoint + f"/segments/legend")
        legend_kills = {}

        highest_kill_count = -1;
        
        for n in range(0, len(legend_data["data"])):
            name = legend_data["data"][n]["metadata"]["name"]
            kills = legend_data["data"][n]["stats"]["kills"]["value"]
            if (highest_kill_count < kills):
                highest_kill_count = kills
                main_legend = name
            legend_kills[name] = kills
            
        k_percentage = "{:.2f}".format(100*highest_kill_count/lifetime_kills)
        print(f"Main legend: {main_legend} with {k_percentage}% of total kills")
        print(legend_kills)



