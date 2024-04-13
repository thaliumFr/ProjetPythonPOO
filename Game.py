from dataclasses import dataclass
import datetime


@dataclass
class Game:
    name: str
    devs: str
    release: datetime
    price: str
    note: float
    platforms: list
    genders: list
    isMultiplayer: bool
    ageLimit: int
    openCriticslink: str = ""
