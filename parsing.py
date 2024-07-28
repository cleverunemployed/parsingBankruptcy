from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
import time


def parsing_data(driver: Chrome, url: str) -> list[list[str]]:
    driver.get(url)
    time.sleep(5)
    result: list[list[str]] = list()

    soup = BeautifulSoup(driver.page_source, 'lxml')

    table = soup.find("table", attrs={"class": "bank"}).find("tbody")
    rows: list = table.find_all("tr")[:-2]

    for tr in rows:
        data: list[str] = []
        if tr.find_all("th") != []:
            for th in tr.find_all("th"):
                data.append(th.text.replace("\n", "").replace("\t", ""))
        else:
            for td in tr.find_all("td"):
                data.append(td.text.replace("\n", "").replace("\t", ""))
        result.append(data)

    return result


def data_collection(url: str) -> list[list[str]]:

    data: list = []
    driver: Chrome = Chrome()

    data = parsing_data(driver=driver, url=url)
    [print(x) for x in data]
    return data


def main() -> None:
    data_collection("https://old.bankrot.fedresurs.ru/TradeList.aspx")


if __name__ == "__main__":
    main()