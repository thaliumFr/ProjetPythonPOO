from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class Crawler:
    url: str = ""
    elements: list = []
    elementsValues: dict[str, list[WebElement]] = {}

    driver: webdriver.Firefox

    def __init__(self, url, elements):
        self.url = url
        self.elements = elements

    def reponse(self):
        driver = webdriver.Firefox()
        driver.get(self.url)
        self.driver = driver

        res = {}
        for element in self.elements:
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element(By.CLASS_NAME, element)
            )
            elements = driver.find_elements(By.CLASS_NAME, element)

            elList = []
            for el in elements:
                elList.append(el)

            res[element] = elList

        self.elementsValues = res

    def end(self):
        self.driver.close()


if __name__ == "__main__":
    crawler_opencritique = Crawler(
        "https://opencritic.com/", ["actual-game-name", "game-name-container"]
    )

    crawler_opencritique.reponse()
    crawler_opencritique.end()
