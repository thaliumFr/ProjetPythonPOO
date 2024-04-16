import datetime
import json
from math import floor
from matplotlib import dates, pyplot as plt
import requests
import time

from multiprocessing import Manager, Process, Array


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
        super().__init__()
        self.appid = appid

    @staticmethod
    def GetAllGames(limit=-1) -> list["SteamGame"]:
        url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + key
        gamesJson = requests.get(url)
        allGames = json.loads(gamesJson.content)["applist"]["apps"]

        if limit > 0:
            allGames = allGames[:limit]

        allGamesLen = len(allGames)
        gamesList = []

        MULTITHREADING = False

        if MULTITHREADING:
            threads = 4
            allProcesses = []

            for i in range(threads):
                mini = floor(i * (allGamesLen / threads))
                maxi = floor((i + 1) * (allGamesLen / threads))
                print(f"starting process from {mini} to {maxi}")
                thread = Process(
                    target=SteamGame.getGameinRange, args=(mini, maxi, gamesList)
                )
                allProcesses.append(thread)

            for thread in allProcesses:
                thread.start()

            for thread in allProcesses:
                thread.join()
        else:
            SteamGame.getGameinRange(0, allGamesLen, gamesList)

        print("Done", flush=True)
        print(gamesList, flush=True)
        return gamesList

    @staticmethod
    def getGameinRange(mini, maxi, gamesList: list):
        start = time.time()
        minmax: tuple = (mini, maxi)
        num = 1
        url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + key
        gamesJson = requests.get(url)
        allGames = json.loads(gamesJson.content)["applist"]["apps"]

        res = []

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
                print("fail to fetch game")
                continue

            if gamedata["type"] != "game":
                continue  # cordialement

            steamGame = SteamGame(
                game["appid"],
            )

            steamGame.name = gamedata["name"]
            steamGame.ageLimit = gamedata["required_age"]
            steamGame.devs = (
                gamedata["developers"] if gamedata.__contains__("developers") else []
            )

            steamGame.platforms = (
                gamedata["platforms"] if gamedata.__contains__("platforms") else []
            )

            steamGame.genders = (
                gamedata["genres"] if gamedata.__contains__("genre") else []
            )

            steamGame.price = (
                gamedata["price_overview"]["final_formatted"]
                if gamedata.__contains__("price_overview")
                else ""
            )

            steamGame.release = (
                SteamGame.getDateFromSteam(gamedata["release_date"]["date"])
                if gamedata["release_date"].__contains__("date")
                else None
            )

            print(steamGame.toList(), flush=True)
            gamesList.append(steamGame)
            res.append(steamGame)
            num += 1

    @staticmethod
    def getGameData(appid) -> list:

        if not isinstance(appid, str):
            appid = str(appid)

        url = "https://store.steampowered.com/api/appdetails?appids=" + appid

        print(url)

        gamedatajson: requests.Response
        try:
            gamedatajson = requests.get(url)
            print(gamedatajson.content)
        except:
            return

        gamedata = json.loads(gamedatajson.content)
        if gamedata == None:
            return

        if not gamedata.__contains__(appid):
            print("cant find appid in json")
            return
        gamedata = gamedata[appid]

        if not gamedata["success"]:
            print("not success for game : " + appid)
            return

        print("SUCCESS AT RETREIVING GAME")
        return gamedata["data"]

    def toList(self):
        return [
            self.appid,
            self.name,
            self.price,
            str(self.release),
            self.devs,
            self.genders,
            self.isMultiplayer,
            self.platforms,
        ]

    @staticmethod
    def getDateFromSteam(date: str) -> datetime:
        vals = date.split(r" ")

        if date.lower().__contains__("announced"):
            return None

        if len(vals) == 3:
            try:
                year = vals[2]
                month = SteamGame._months[vals[1].rstrip(",")]
                day = vals[0]
            except:
                year = vals[2]
                month = SteamGame._months[vals[0].rstrip(",")]
                day = vals[1].rstrip(",")
        else:
            year = date[-4:]
            return f"{year}"
        return f"{day}-{month}-{year}"
