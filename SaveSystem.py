class Csv:
    content: list[list] = []
    name: str = "default"

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
        with open(self.name + ".csv", "w") as file:
            txt = []

            for i in self.content:
                txt.append(",".join(i) + "\n")

            file.writelines(txt)

    @staticmethod
    def Load(name: str) -> "Csv":
        content = []
        with open(name + ".csv", "r") as file:
            for i in file.readlines():
                line = i.split(",")
                line[-1] = line[-1].rstrip("\n")
                content.append(line)

        csv = Csv(name)
        csv.content = content
        return csv

    def Add(self, line: list[str]):
        self.content.append(line)
