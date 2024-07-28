from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By


def save_data(data: list) -> None:
    with open('sw_data_new.csv', 'w', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(data[0])
        for row in data[1:]:
            if row[0] != "Номер торгов":
                print(row[0])
                writer.writerow(row)


def parsing_data(driver: Chrome) -> list[list[str]]:
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
    pagination_page: int = 2
    option = ChromeOptions()

    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument("--headless=new")
    option.add_argument('--disable-gpu')
    option.add_argument('--enable-javascript')
    option.add_argument('--no-sandbox')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--allow-insecure-localhost')
    option.add_argument("--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'")
    driver: Chrome = Chrome(options=option)
    driver.get(url)

    while True:
        for i in parsing_data(driver=driver):
            data.append(i)

        elements = driver.find_element(by=By.CLASS_NAME, value="pager").find_element(by=By.TAG_NAME, value="tr").find_elements(by=By.TAG_NAME, value="td")
        for el in elements[1:]:
            try:
                el = el.find_element(by=By.TAG_NAME, value="a")
            except:
                pass
            if el.text == str(pagination_page):
                driver.execute_script("arguments[0].click();", el)
                break
            elif el.text == "..." and pagination_page%10 == 1:
                driver.execute_script("arguments[0].click();", el)
                break

        pagination_page += 1
        print(f"[+] correct {pagination_page}")

        if pagination_page > 15:
            break
    
    return data


def main() -> None:
    data = data_collection("https://old.bankrot.fedresurs.ru/TradeList.aspx")
    save_data(data=data)


if __name__ == "__main__":
    main()