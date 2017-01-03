__author__ = "Shensd"

from .player import player
import requests

class client(object):
    def __init__(self, api_key, verify=True):
        self.api_key = api_key
        if verify:
            try:
                r = requests.get("http://google.com")
                r.close()
            except Exception:
                raise Exception("Unable to connect to internet.")
            try:
                r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids=76561197960435530".format(api_key))
                r.close()
            except Exception:
                raise Exception("Invalid API key")
    def new_player(self, player_id):
        return player(self.api_key, player_id)
    def new_app(self, app_id):
        return app(app_id)
