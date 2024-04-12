from SteamAPI import SteamGame
from crawler import Crawler

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from SaveSystem import Csv
import matplotlib.pyplot as plt
from time import sleep

maxPagesOnOpenCritics = 766


crawler_opencritique = Crawler(
    "https://opencritic.com/browse/all/all-time/name?page=",
    ["game-name"],
)

OpenCriticsGames = Csv("OpenCritics")
OpenCriticsGames.Add(["Name", "link"])

allLinks = []
for i in range(maxPagesOnOpenCritics):

    crawler_opencritique.driver.get(crawler_opencritique.url + str(i + 1))

    crawler_opencritique.reponse()

    for el in crawler_opencritique.elementsValues["game-name"]:
        try:
            a = el.find_element(By.TAG_NAME, "a")
            link = a.get_attribute("href")
            print(link)
            allLinks.append(link)

            OpenCriticsGames.Add([a.text, link])
        except:
            pass

OpenCriticsGames.Save()


for link in allLinks:
    crawler_opencritique.driver.get(link)

    crawler_opencritique.reponse()

crawler_opencritique.end()


# API
SteamGames = Csv("SteamGames")
SteamGames.Add(["appid", "name", "price"])
for game in SteamGame.GetAllGames():
    # print(game)
    SteamGames.Add(game.toList())

SteamGames.Save()
