from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup
import re


# phrase = input("Podaj szukaną frazę:").strip().replace(" ", "+")


def google_web_page(phrase):
    google_html = 'https://www.google.com/search?q='
    start_url = google_html + phrase
    try:
        req = Request(start_url, headers={'User-Agent': 'Mozilla/5.0'})
        req.add_header('Accept-Encoding', 'utf-8')

        web_byte = urlopen(req).read()

        webpage = web_byte.decode('utf-8')
        return webpage
    except HTTPError:
        print('Something went wrong - HTTP Error')
    except URLError:
        print('Page could not be found')


def get_external_links(url=None, bs_obj=None):
    if url is not None:
        bs_obj = BeautifulSoup(url, 'html.parser')
    elif bs_obj is None:
        raise ValueError(
            'Required url=urlopen(url).read() argument or bs_obj=BeautifulSoup(url, "parser_name") object. You gave none of them.')

    all_links = bs_obj.findAll("a")

    if len(all_links) == 0:
        return None

    for link in all_links:
        if 'href' in link.attrs:
            page = link.attrs['href']
            if page.startswith(r"/url?q="):
                if 'google' not in page:
                    u = urlparse(page[7:])
                    yield urlunparse((u.scheme, u.netloc, '', '', '', ''))


def get_next_page(url=None, bs_obj=None):
    if url is not None:
        bs_obj = BeautifulSoup(url, 'html.parser')
    elif bs_obj is None:
        raise ValueError(
            'Required url=urlopen(url).read() argument or bs_obj=BeautifulSoup(url, "parser_name") object. You gave none of them.')

    # print(bs_obj.prettify())
    all_links = bs_obj.findAll("a")
    for link in all_links:
        print(link.attrs['href'])


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

    # dodanie linku do listy ( bazy danych )
    # tworzy bazę danych na podstawie wpisanej kategorii np. biura architektoniczne łódź
    # sprawdza czy dany link widnieje już w bazie danych oraz czy nie jest na black liście:
    # wikipedia, google, amazon, allegro , wp, onet itp.
