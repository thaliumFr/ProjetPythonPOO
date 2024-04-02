from bs4 import BeautifulSoup
import requests


class Crawler:
    url: str = ""
    elements: list = []


    def __init__(self, url, elements):
        self.url = url 
        self.elements = elements

    def reponse(self):
        reponse = requests.get(self.url)
        if reponse.status_code == 200:
            soup = BeautifulSoup(reponse.text, 'html.parser')
            for element in self.elements:
                split = element.split(".")
                elementname = split[0]
                classname = split[1] 
                found_elements = soup.find_all(elementname, class_=classname)
                print(found_elements, elementname, classname)
                
        else:
            print('erreur lors du téléchargement de la page: erreur ', reponse.status_code)

crawler_opencritique = Crawler('https://opencritic.com/', ["div.actual-game-name"]) 

crawler_opencritique.reponse()