class Csv:
    content: list[list] = []
    name: str = "default"

    __separator = ";"

    def __init__(self, name: str) -> None:
        self.content = []
        self.name = name

    @property
    def lines(self):
        return len(self.content)

    @property
    def columns(self):
        maxCol = 0

        for i in self.content:
            if len(i) > maxCol:
                maxCol = len(i)
        return maxCol

    def Save(self):
        with open(self.name + ".csv", "w", encoding="utf-8") as file:
            for line in self.content:

                goodLine = []
                for word in line:
                    goodLine.append('"' + word + '"')

                file.write(Csv.__separator.join(goodLine) + "\n")

    @staticmethod
    def Load(name: str) -> "Csv":
        content = []
        with open(name + ".csv", "r", encoding="utf8") as file:
            for i in file.readlines():
                i = i.rstrip("\n")
                import re

                PATTERN = re.compile(r"""((?:[^,"']|"[^"]*"|'[^']*')+)""")

                content.append(PATTERN.split(i)[1::2])

        csv = Csv(name)
        csv.content = content
        return csv

    def Add(self, line: list[str]):
        self.content.append(line)

    def AddToLine(self, y: int, line: list[str] | str):
        if isinstance(line, list):
            for el in line:
                self.content[y].append(el)
        else:
            self.content[y].append(line)

    def hasInColumn(self, txt, col=0):
        for i in self.content:
            if i[col] == txt:
                return True
        return False

    def CountInColumn(self, txt: str, col=0, caseSensitive=False):
        count = 0
        if not caseSensitive:
            txt = txt.lower()
        for i in self.content:
            data: str = i[col]
            if not caseSensitive:
                data = data.lower()
            if data == txt:
                count += 1
        return count

    def hasInRow(self, txt: str, row=0):
        return self.content[row].__contains__(txt)

    def FindInColumn(self, txt, col=0):
        for i in range(self.columns - 1):
            if self.content[i][col].lower() == txt.lower():
                return i
        return -1

    def GetColumn(self, i: int):
        data = []
        for el in self.content:
            data.append(el[i])

        return data

    def GetRow(self, i: int):
        return self.content[i]
