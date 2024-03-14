class Csv:
    content: list[list] = []
    name: str = "default"

    def __init__(self, name: str) -> None:
        self.content = []
        self.name = name

    @property
    def lines(self):
        return len(self.content)

    def Save(self):
        with open(self.name + ".csv", "w") as file:
            txt = []

            for i in self.content:
                txt.append(",".join(i))

            file.writelines(txt)

    @staticmethod
    def Load(name: str) -> "Csv":
        content = []
        with open(name + ".csv", "r") as file:
            for i in file.readlines():
                content.append(i.split(","))

        csv = Csv(name)
        csv.content = content
        return csv
