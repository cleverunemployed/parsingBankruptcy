import csv
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions 

# функция для сохранения результата парсинга в sw_data_new.csv
# принимает список списков
def save_data(data: list) -> None:

    # создаём файл под кодировку 'utf-8' для записи, каждая новая строка заканчиваеться пустым символом 
    with open('sw_data_new.csv', 'w+', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";") # создаём csv таблицу

        writer.writerow(data[0]) # записываем первую строку, так как она являеться 'шапкой' таблицы

        for row in data[1:]: # записываем все остальные строки, кроме начальных
            if row[0] != "Номер торгов":
                writer.writerow(row)

# функция сбора данных с одной страницы
# принимает WebDriver
def parsing_data(driver: Chrome) -> list[list[str]]:
    # время для прогрузки страницы
    time.sleep(5)
    # выходной результат
    result: list[list[str]] = list()
    # создаём объект для поиска нужной информации
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # поиск нужных блоков с информации
    table = soup.find("table", attrs={"class": "bank"}).find("tbody")
    rows: list = table.find_all("tr")[:-2]

    for tr in rows:
        data: list[str] = []
        # проверка на "первую" строку
        if tr.find_all("th") != []:
            for th in tr.find_all("th"):
                data.append(th.text.replace("\n", "").replace("\t", ""))
        else:
            for td in tr.find_all("td"):
                data.append(td.text.replace("\n", "").replace("\t", ""))
        result.append(data)

    return result

# функция для заготовки данных
# принимает url
def data_collection(url: str) -> list[list[str]]:

    data: list[list[str]] = [] # итоговый спиок
    pagination_page: int = 2 # текущая страница

    option = ChromeOptions() # опции для WebDriver

    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument("--headless=new")
    option.add_argument('--disable-gpu')
    option.add_argument('--enable-javascript')
    option.add_argument('--no-sandbox')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--allow-insecure-localhost')
    option.add_argument("--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'")
    driver: Chrome = Chrome(options=option) # драйвер
    driver.get(url) # делаем запрос по url

    # цикл проходящий по страницам сайта
    while True:

        # добавляем данные в итоговый список по строчно
        for i in parsing_data(driver=driver):
            data.append(i)

        # поиск следующей страницы
        elements = driver.find_element(by=By.CLASS_NAME, value="pager").find_element(by=By.TAG_NAME, value="tr").find_elements(by=By.TAG_NAME, value="td")
        for el in elements[1:]:
            # проверка 
            try:
                el = el.find_element(by=By.TAG_NAME, value="a")
            except:
                pass
            if el.text == str(pagination_page):
                driver.execute_script("arguments[0].click();", el)
                break
            elif el.text == "..." and pagination_page%10 == 1: # проверка на последнюю страницу
                driver.execute_script("arguments[0].click();", el)
                break
        else: # если страница не попала ни в одну катешорию, то это была последняя страница
            break    
        
        pagination_page += 1 # инкрементация количества страниц
        print(f"[+] correct {pagination_page}") # псевдо логирование
    
    return data

# главная фкнкция
def main() -> None:
    data = data_collection("https://old.bankrot.fedresurs.ru/TradeList.aspx")
    save_data(data=data)

# точка входа
if __name__ == "__main__":
    main()