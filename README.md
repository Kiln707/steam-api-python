# Python Steam API
An unofficial steam API for python

## What is it
This is an unofficial Steam API written in python, making it easy to get information about store apps and Steam users. It works by using the [Requests](https://github.com/kennethreitz/requests) package to retrieve information from Steam's web API (more info on Steam's API can be found [here](https://developer.valvesoftware.com/wiki/Steam_Web_API)).

## How to use it
Steam_api is object oriented, and works by making a client with a [Steam API key](https://steamcommunity.com/dev/apikey) and then making player objects from there. Getting store app information does not require an API key so `app` objects do not need to be made through a client object.

Here are a few examples:
```python
from steam_api import client, player, app

my_client = client("XXXXXXXXXXXXXXXX") #Put your Steam API key here!
my_player = my_client.new_player("76561198075159344") #that's me!
my_app = app(440) #Team Fortress 2

print("Profile Name     :", my_player.get_profile_name())
print("Profile ID       :", my_player.get_steam_id())
print("Number of friends:",my_player.get_num_friends())

print("App Name         :", my_app.get_app_name())
print("App ID           :", my_app.get_app_id())
print("Store Page URL   :", my_app.get_app_storepage_url())
```
Running that with a valid API key will return:
```
Profile Name     : SHENANIGANS
Profile ID       : 76561198075159344
Number of friends: 188
App Name         : Team Fortress 2
App ID           : 440
Store Page URL   : http://store.steampowered.com/app/440/
```
## How to install it
Download the repository and run `python setup.py install` and it will be install globally on the system. Once it is installed it can be imported and used in projects as shown above.

## Other Things

- This API is unofficial
- This is still being developed so stay tuned for updates!
- This is my first python package so advice and suggestions are welcome!
- You can get an API key at https://steamcommunity.com/dev/apikey
- This is works off of the Steam Web API so if the Web API is down, so is this app!
- This app isn't exactly the fastest thing in the world, so be wary with what you use it with, it could end up being the bottleneck in your project
- This is Licensed under the MIT Open Source License
