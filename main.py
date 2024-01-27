import requests
from bs4 import BeautifulSoup
import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('links.db')
c = conn.cursor()

# Создаем таблицу для хранения ссылок
c.execute('''CREATE TABLE IF NOT EXISTS links
             (id INTEGER PRIMARY KEY, url text)''')

# Функция для скрапинга информации с веб-страницы
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Добавляем код для поиска нужной информации и сохранения её

# Функция для поиска новых ссылок на странице и их сохранения в базу данных
def find_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            # Проверяем, что ссылка удовлетворяет нашим требованиям
            if href:
                # Добавляем проверку, чтобы избежать дублей
                c.execute("INSERT INTO links (url) VALUES (?)", (href,))
    conn.commit()

# Пример использования функций
start_url = 'https://example.com'
find_links(start_url)

# Закрываем соединение с базой данных
conn.close()