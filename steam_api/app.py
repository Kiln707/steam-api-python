__author__ = "Shensd"

import requests

class app(object):
    def __init__(self, app_id, verify=True):
        self.app_id = app_id
        if not self._get_json(self.get_app_details())[str(self.app_id)]["success"]:
            raise Exception("Invalid App ID")

    def get_app_storepage_url(self):
        url = "http://store.steampowered.com/app/{}/".format(self.app_id)
        return url
    def get_app_details(self):
        url = "http://store.steampowered.com/api/appdetails?appids={}".format(self.app_id)
        return url
    def get_achievement_url(self):
        url = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={}&format=json".format(self.app_id)
        return url
    def get_app_news_url(self):
        url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={}&count=3&maxlength=300&format=json".format(self.app_id)

    def _get_json(self, url):
        r = requests.get(url)
        return r.json()

    def get_app_name(self):
        return self._get_json(self.get_app_details())[str(self.app_id)]["data"]["name"]
    def get_app_id(self):
        return self.app_id
