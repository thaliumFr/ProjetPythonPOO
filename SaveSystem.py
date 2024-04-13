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
        with open(name + ".csv", "r") as file:
            for i in file.readlines():
                line = i.split(Csv.__separator)
                line[-1] = line[-1].rstrip("\n").strip('"')
                content.append(line)

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
