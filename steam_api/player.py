__author__ = "Shensd"

import requests, datetime

class player(object):
    def __init__(self, api_key, player_id):
        self.api_key = api_key
        self.player_id = player_id

        r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(self.api_key, self.player_id))
        self.player_json = r.json()

    def get_api_url(self):
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(self.api_key, self.player_id)
        return url
    def get_profile_url(self):
        url = "http://steamcommunity.com/profiles/{}".format(self.player_id)
        return url
    def get_friend_list_url(self):
        url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={}&steamid={}&relationship=friend".format(self.api_key, self.player_id)
        return url
    def get_recently_played_url(self):
        url = "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={}&steamid={}&format=json".format(self.api_key, self.player_id)
        return url
    def get_achievement_url(self, app_id):
        url = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={}&key={}&steamid={}".format(app_id, self.api_key, self.player_id)
        return url
    def get_games_url(self):
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&format=json".format(self.api_key, self.player_id)
        return url
    def _get_json(self, url):
        r = requests.get(url)
        return r.json()

    def get_attr(self):
        return self.player_json["response"]["players"][0]

    def get_steam_id(self):
        return self.get_attr()["steamid"]
    def get_community_state(self):
        return self.get_attr()["communityvisibilitystate"]
    def get_profile_state(self):
        return self.get_attr()["profilestate"]
    def get_profile_name(self):
        return self.get_attr()["personaname"]
    def get_personastate(self):
        return self.get_attr()["personastate"]
    def get_real_name(self):
        return self.get_attr()["realname"]
    def get_primary_clan_id(self):
        return self.get_attr()["primaryclanid"]
    def get_country_code(self):
        return self.get_attr()["loccountrycode"]
    def get_state_code(self):
        return self.get_attr()["locstatecode"]
    def get_city_id(self):
        return self.get_attr()["loccityid"]
    def get_avatar_url_small(self):
        return self.get_attr()["avatar"]
    def get_avatar_url_medium(self):
        return self.get_attr()["avatarmedium"]
    def get_avatar_url_full(self):
        return self.get_attr()["avatarfull"]
    def get_last_logoff(self, date=False):
        last = self.get_attr()["lastlogoff"]
        if date:
            return datetime.datetime.fromtimestamp(int(last)).strftime('%m/%d/%Y %H:%M:%S')
        else:
            return last
    def get_time_created(self, date=False):
        created = self.get_attr()["timecreated"]
        if date:
            return datetime.datetime.fromtimestamp(int(created)).strftime('%m/%d/%Y %H:%M:%S')
        else:
            return created

    def get_player_summary(self):
        end = ""
        end += "Player Name: {}\n".format(self.get_profile_name())
        end += "Player Id: {}\n".format(self.get_steam_id())
        end += "Last Logoff: {}\n".format(self.get_last_logoff(date=True))
        end += "Number of Friends: {}\n".format(self.get_num_friends())
        end += "Number of Games: {}\n".format(self.get_num_games())
        end += "User Since: {}\n".format(self.get_time_created(date=True))
        return end

    def get_recently_played_games(self):
        return self._get_json(self.get_recently_played_url())["response"]["games"]
    def get_all_games(self):
        return self._get_json(self.get_games_url())["response"]["games"]
    def get_num_games(self):
        return int(self._get_json(self.get_games_url())["response"]["game_count"])

    def get_all_friends(self):
        return self._get_json(self.get_friend_list_url())["friendslist"]["friends"]
    def get_num_friends(self):
        return len(self.get_all_friends())

    def get_app_achievements(self, app_id, achieved=False):
        if achieved:
            chi = []
            for r in self._get_json(self.get_achievement_url(app_id))["playerstats"]["achievements"]:
                if r["achieved"] == 1:
                    chi.append(r)
            return r
        else:
            return self._get_json(self.get_achievement_url(app_id))["playerstats"]["achievements"]
