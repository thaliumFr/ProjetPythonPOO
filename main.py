from SteamAPI import SteamGame
from SaveSystem import Csv
import matplotlib.pyplot as plt


SteamGames = Csv("SteamGames")
SteamGames.Add(["appid", "name", "price"])
for game in SteamGame.GetAllGames():
    # print(game)
    SteamGames.Add(game.toList())

SteamGames.Save()
