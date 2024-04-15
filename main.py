import time
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
OpenCriticsGames.Add(
    [
        "Name",
        "link",
        "devs",
        "release",
        "note AVG",
        "critics recommend",
        "price",
        "isMultiplayer",
        "ageLimit",
    ]
)


def CrawlOpenCritics():
    start = time.time()

    allLinks = []
    for y in range(1):
        crawler_opencritique.driver.get(crawler_opencritique.url + str(y + 1))

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

    crawler_opencritique.end()

    pageDetailsClasses = [
        "companies",
        "platforms",
        "inner-orb",
    ]
    crawler_pageDetails = Crawler("https://opencritic.com/", pageDetailsClasses)
    games = []
    y = 0
    for link in allLinks:
        crawler_pageDetails.driver.get(link)

        crawler_pageDetails.reponse()

        for classname in pageDetailsClasses:
            if crawler_pageDetails.elementsValues.__contains__(classname):
                TextVals = []
                # Companies
                for el in crawler_pageDetails.elementsValues[classname]:
                    txt = el.text

                    if classname == pageDetailsClasses[1]:
                        txt = txt.split("-")[0].strip()

                    TextVals.append(txt)

                OpenCriticsGames.AddToLine(y + 1, TextVals)

        lineLength = len(OpenCriticsGames.content[y + 1])
        expectedLenght = 6
        for x in range(expectedLenght - lineLength):
            OpenCriticsGames.AddToLine(y + 1, "none")

        y += 1

    OpenCriticsGames.Save()
    crawler_pageDetails.end()

    end = time.time()

    print(f"Crawl ended in {end-start} seconds")


# API
# SteamGames = Csv("SteamGames")
# SteamGames.Add(["appid", "name", "price"])
# for game in SteamGame.GetAllGames():
#     # print(game)
#     SteamGames.Add(game.toList())

# SteamGames.Save()

if __name__ == "__main__":
    CrawlOpenCritics()
