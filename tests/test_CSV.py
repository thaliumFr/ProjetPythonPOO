from SaveSystem import Csv


def test_SaveSystem():
    csv = Csv("ui")

    csv.content.append(["nom", "prix", "score", "taille Gb"])
    csv.content.append(["35", "24", "56", "34", "56"])

    print(csv.lines)

    csv.Save()
    csv2 = Csv.Load("ui")
    print(csv2)

    assert csv2.content == csv.content


def test_line():
    csv = Csv("ui")

    csv.content.append(["nom", "prix", "score", "taille Gb"])
    csv.content.append(["35", "24", "56", "34", "56"])
    assert csv.lines == 2


def test_column():
    csv = Csv("ui")

    csv.content.append(["nom", "prix", "score", "taille Gb"])
    csv.content.append(["35", "24", "56", "34", "56"])
    assert csv.columns == 5
