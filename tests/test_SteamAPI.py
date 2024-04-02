from SteamAPI import SteamGame


def test_dateConverter():
    assert SteamGame.getDateFromSteam("24 Feb, 2023") == "24-02-2023"
