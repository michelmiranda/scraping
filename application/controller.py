from urllib.parse import urlparse

from bs4 import BeautifulSoup
from os import path
import requests
import re
from clint.textui import progress

from book import Book


def getPage(url):
    try:
        req = requests.get(url).text
    except requests.RequestException:
        print(f'Erro na requisição: {url}')
    return BeautifulSoup(req, 'html.parser')


def scrapeBook(url):
    bs = getPage(url)
    url = bs.select('.test-bookpdf-link')[0]['href']
    name = bs.find('div', class_='page-title').find('h1').text
    year = re.findall('(\d{4})', bs.find('span', id='copyright-info').text)[0]
    return Book(url, name, year)


def getDownload(Book, owner):
    name_file_pdf = Book.name +' - '+Book.year
    name_file_pdf = re.sub('/', '-', name_file_pdf)
    if path.exists(name_file_pdf):
        print(f'Esse livro já foi baixado: {name_file_pdf}')
    else:
        with open(name_file_pdf, 'wb') as f:
            print(f'Downloading: {name_file_pdf}')
            resp = requests.get(owner+Book.url, stream=True)

            content_length = int(resp.headers.get('content-length'))
            for chunk in progress.bar(resp.iter_content(chunk_size=1024), expected_size=(content_length/1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
