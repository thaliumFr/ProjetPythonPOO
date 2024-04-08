from SteamAPI import SteamGame
from crawler import Crawler

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from SaveSystem import Csv
import matplotlib.pyplot as plt
from time import sleep


maxPagesOnOpenCritics = 766

for i in range(10):
    crawler_opencritique = Crawler(
        "https://opencritic.com/browse/all/all-time/name?page=" + str(i + 1),
        ["game-name"],
    )

    crawler_opencritique.reponse()

    for el in crawler_opencritique.elementsValues["game-name"]:
        print(
            el.get_attribute("href"),
            el.find_element(By.TAG_NAME, "a").get_attribute("href"),
        )


# API
SteamGames = Csv("SteamGames")
SteamGames.Add(["appid", "name", "price"])
for game in SteamGame.GetAllGames():
    # print(game)
    SteamGames.Add(game.toList())

SteamGames.Save()
