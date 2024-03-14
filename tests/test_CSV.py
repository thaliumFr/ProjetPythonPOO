def test_SaveSystem():
    from SaveSystem import Csv

    csv = Csv("ui")

    csv.content.append(["nom", "prix", "score", "taille Gb"])
    csv.content.append(["35", "24", "56", "34"])

    print(csv.lines)

    csv.Save()
    csv2 = Csv.Load("ui")
    print(csv2)

    assert csv2.content == csv.content
