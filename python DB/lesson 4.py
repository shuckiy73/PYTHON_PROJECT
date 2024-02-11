import requests
from bs4 import BeautifulSoup
import pandas

# pip install beautifulsoup4
# pip install pandas


def get_mebel_items(link):
    response = requests.get(link)
    mebel_data = response.text

    mebel_items = []
    to_parse = BeautifulSoup(mebel_data, 'html.parser')
    for elem in to_parse.find_all('a', class_='styles_wrapper__yaLfq'):
        mebel_items.append((elem['href'], elem.text))

    return mebel_items


def save_to_csv(mebel_items):
    pandas.DataFrame(mebel_items).to_csv('mebel.csv', index=False)


def run():
    mebel_items = get_mebel_items('https://www.kufar.by/l/mebel')
    save_to_csv(mebel_items)


run()
