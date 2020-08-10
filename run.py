from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup
import re
import requests
from requests import HTTPError, ConnectionError
import csv


class GoogleSearch:
    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase = self.phrase.replace(' ', '+')

        self.url = f"https://google.pl/search?q={self.phrase}"

    def get_page(self, page='phrase'):
        if page == 'phrase':
            url = self.url
        else:
            url = page

        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        # MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
        headers = {"user-agent": USER_AGENT}
        try:
            req = requests.get(url, headers=headers)
            if req.status_code == 200:
                soup = BeautifulSoup(req.content, "lxml")
                return soup
        except ConnectionError:
            raise ConnectionError(
                'Probably you have used incorrect link!')

    def get_external_links(self, bs_obj):
        for link in bs_obj.find_all("div", {"class": "r"}):
            link = link.find("a")
            if 'href' in link.attrs:
                page_url = link.attrs['href']
                if 'google' not in page_url:
                    page_url = urlparse(page_url)
                    yield urlunparse((page_url.scheme, page_url.netloc, '', '', '', ''))

    def get_next_pages(self, bs_obj):
        pages_dict = dict()
        pages_links = bs_obj.find_all("a", {"class": "fl"})

        for page_link in pages_links:
            try:
                key_value = str(page_link['aria-label'])
                if key_value not in pages_dict.keys():
                    pages_dict[key_value] = f"https://google.com{page_link['href']}"
            except ValueError:
                pass
            except KeyError:
                pass
        return pages_dict

    def get_soup(self, url):
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
        headers = {"user-agent": USER_AGENT}
        try:
            req = requests.get(url, headers=headers)
            if req.status_code == 200:
                soup = BeautifulSoup(req.content, "html.parser")
                return soup
        except ConnectionError:
            raise ConnectionError(
                'Probably you have used incorrect link!')


external_links_list = []
page = GoogleSearch('biura architektoniczne warszawa')
soup = page.get_page()
links = page.get_external_links(soup)
for link in links:
    external_links_list.append(link)

pages_dict = page.get_next_pages(soup)
for page_number in range(2, 8):
    soup = page.get_page(pages_dict[f'Page {page_number}'])
    links = page.get_external_links(soup)
    with open('external_link_test.csv', 'a+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['id', 'link'])
        for iteration, link in enumerate(links):
            writer.writerow([iteration+1, link])
# print(len(external_links_list))
# print(external_links_list)


'''
def black_list_remove(link):
    black_list = [
        'https://pl.wikipedia.org',
        'https://www.google.pl',
        'https://www.yahoo.com'
    ]
    if link not in black_list:
        return link
    else:
        return None


if __name__ == "__main__":
    external_links_list = []
    phrase = 'biura+architektoniczne+warszawa'
    webpage = google_web_page(phrase)
    bsObj = BeautifulSoup(webpage, 'lxml')
    if webpage != None:
        links = get_external_links(bs_obj=bsObj)
        for link in links:
            if black_list_remove(link) != None:
                external_links_list.append(link)

    print(external_links_list)

    # SEKCJA: Pobieranie kolejnej strony z google
    get_next_page(bs_obj=bsObj)

    # dodanie linków do bazy danych mysql (tworzy bazę danych na podstawie wpisanej kategorii np. biura architektoniczne łódź = biura_architektoniczne_lodz)
    # kolumny = (id, data_pierwszego dodania, ostatnia aktualizacja, nazwa firmy, strona internetowa, przeszukana strona - Tak lub Nie, mail, nr telefonu, fax, Ulica, Miejscowość, Kod pocztowy, KRS, NIP, REGON, Kapitał zakładowy, Forma prawna, Data Rejestracji, Ostatnia zmiana w KRS, Reprezentacja, Sposób reprezentacji, Sąd, Sygnatura, Podstawowa działalność, Wspólnicy, Zarząd, Prokura, Właściciel)
    # stworzenie bazy danych black listy (wikipedia, google, amazon, allegro , wp, onet itp.)
    # pobranie linku z bazy 
'''
