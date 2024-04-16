from dataclasses import dataclass, field
import datetime


@dataclass
class Game:
    name: str = ""
    devs: str = ""
    release: datetime = ""
    price: str = ""
    note: float = 0
    platforms: list = field(default_factory=list)
    genders: list = field(default_factory=list)
    isMultiplayer: bool = False
    ageLimit: int = 0
    openCriticslink: str = ""
