from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
import time


def data_collection(url: str) -> list[list[str]]:

    data: list = []
    driver: Chrome = Chrome()
    driver.get(url=url)

    time.sleep(5)

    


    return list


def main() -> None:
    data_collection("https://old.bankrot.fedresurs.ru/TradeList.aspx")


if __name__ == "__main__":
    main()