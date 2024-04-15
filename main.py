import time
from SteamAPI import SteamGame
from crawler import Crawler

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from SaveSystem import Csv
import matplotlib.pyplot as plt

import threading

from GraphDisplay import GraphDisplay

maxPagesOnOpenCritics = 766
DoCrawl = False
DoAPI = True

pageDetailsClasses = [
    "companies",
    "platforms",
    "inner-orb",
]

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


def CrawlOpenCritics(Multithreading=True):
    start = time.time()
    crawler_opencritique = Crawler(
        "https://opencritic.com/browse/all/all-time/name?page=",
        ["game-name"],
    )

    allLinks = []
    for y in range(2):
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

    games = []

    threads = 4
    # for thread in range(threads):
    #     linksRange =

    #     process = threading.Thread(target=crawlLinks, args=())
    #     process.start()
    #     process.join()

    crawlLinks(allLinks)

    OpenCriticsGames.Save()

    end = time.time()

    print(f"Crawl ended in {end-start} seconds")


def crawlLinks(allLinks):
    y = 1
    crawler_pageDetails = Crawler("https://opencritic.com/", pageDetailsClasses)
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

                OpenCriticsGames.AddToLine(y, TextVals)

        lineLength = len(OpenCriticsGames.content[y])
        expectedLenght = 6
        for x in range(expectedLenght - lineLength):
            OpenCriticsGames.AddToLine(y, "none")

        y += 1

    crawler_pageDetails.end()


if __name__ == "__main__":
    if DoCrawl:
        CrawlOpenCritics()

    if DoAPI:
        # API
        SteamGames = Csv("OpenCritics")
        for game in SteamGame.GetAllGames():
            if SteamGames.hasInColumn(game.name):
                SteamGames.AddToLine(SteamGames.FindInColumn(game.name), game.price)

    data = Csv.Load("OpenCritics")

    NoteSum = 0
    points = []
    for y in range(data.lines - 2):
        note = data.content[y + 1][4].strip('"')
        date = data.content[y + 1][3].strip('"')[-4::]
        print(date)

        if note == "none":
            continue
        NoteSum += int(note)

        points.append((int(date), int(note)))

    GraphDisplay.show2setsPlots(
        "Note per game on years", [points], x_name="Year of release", y_name="Score"
    )

    print(NoteSum, NoteSum / (data.lines - 1))
