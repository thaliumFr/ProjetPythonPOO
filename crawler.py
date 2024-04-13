from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class Crawler:
    url: str = ""
    elements: list = []
    elementsValues: dict[str, list[WebElement]] = {}

    driver: webdriver.Firefox

    __timeout = 5

    def __init__(self, url, elements):
        self.url = url
        self.elements = elements
        driver = webdriver.Firefox()
        self.driver = driver

    def reponse(self):
        driver = self.driver

        res = {}
        for element in self.elements:
            try:
                WebDriverWait(driver, self.__timeout).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, element)
                )
            except:
                self.elementsValues = res
                return
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
