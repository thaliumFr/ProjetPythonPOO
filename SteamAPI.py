import datetime
import json
from math import floor
from matplotlib import dates, pyplot as plt
import requests
import time

from multiprocessing import Process


from Game import Game

key = "06FC90592BA536743D3365CDF555E80A"


class SteamGame(Game):
    appid: str

    _months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    def __init__(self, appid) -> None:
        super.__init__()
        self.appid = appid

    @staticmethod
    def GetAllGames() -> list["SteamGame"]:
        url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + key
        gamesJson = requests.get(url)
        allGames = json.loads(gamesJson.content)["applist"]["apps"]
        allGamesLen = len(allGames)
        gamesList = []

        threads = 8
        allProcesses = []
        for i in range(threads):
            mini = floor(i * (allGamesLen / threads))
            maxi = floor((i + 1) * (allGamesLen / threads))
            print(f"starting process from {mini} to {maxi}")
            thread = Process(
                target=SteamGame.getGameinRange, args=((mini, maxi), gamesList)
            )
            allProcesses.append(thread)

        for thread in allProcesses:
            thread.start()

        for thread in allProcesses:
            thread.join()

        print("Done", flush=True)

        return gamesList

    def getGameinRange(minmax: tuple, gamesList):
        start = time.time()
        num = 1
        url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + key
        gamesJson = requests.get(url)
        allGames = json.loads(gamesJson.content)["applist"]["apps"]
        allGamesLen = len(allGames)
        for game in range(minmax[0], minmax[1]):
            game = allGames[game]
            current = time.time()
            if num % 10 == 0:
                print(
                    f"{num}/{minmax[1]-minmax[0]} done ({round(num/(minmax[1]-minmax[0])*100, 3)}%) in {round((current-start)/(10^9), 2)}s"
                )

            gamedata = SteamGame.getGameData(str(game["appid"]))

            if gamedata == None:
                num += 1
                continue

            steamGame = SteamGame(
                game["appid"],
                gamedata["steam_appid"],
                (
                    gamedata["price_overview"]["final_formatted"]
                    if gamedata.__contains__("price_overview")
                    else ""
                ),
                (
                    SteamGame.getDateFromSteam(gamedata["release_date"]["date"])
                    if gamedata["release_date"]["coming_soon"] == "true"
                    else None
                ),
            )

            gamesList.append(steamGame)
            num += 1

    @staticmethod
    def getGameData(appid) -> list:

        if not isinstance(appid, str):
            appid = str(appid)

        url = "https://store.steampowered.com/api/appdetails?appids=" + appid
        gamedatajson: requests.Response
        try:
            gamedatajson = requests.get(url)
        except:
            return

        if gamedatajson.status_code != "200":
            return

        gamedata = json.loads(gamedatajson.content)
        if not gamedata.__contains__("appid"):
            return
        gamedata = gamedata[appid]

        if not gamedata["success"]:
            return

        return gamedata["data"]

    def toList(self):
        return [self.appid, self.name, self.price, str(self.release)]

    @staticmethod
    def getDateFromSteam(date: str) -> datetime:
        vals = date.split(r" ")
        day = vals[0]
        month = SteamGame._months[vals[1].rstrip(",")]
        year = vals[2]
        return f"{day}-{month}-{year}"
