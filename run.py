from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re


# phrase = input("Podaj szukaną frazę:").strip().replace(" ", "+")


def google_web_page(phrase):
    google_html = 'https://www.google.com/searwch?q='
    start_url = google_html + phrase
    try:
        req = Request(start_url, headers={'User-Agent': 'Mozilla/5.0'})
        req.add_header('Accept-Encoding', 'utf-8')

        web_byte = urlopen(req).read()

        webpage = web_byte.decode('utf-8')
        return webpage
    except HTTPError:
        return(print(HTTPError))
    except URLError:
        print('Page could not be found')
    else:
        print('It worked')


def get_links(url):
    bsObj = BeautifulSoup(url, 'html.parser')
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            page = link.attrs['href']
            if page.startswith(r"/url?q="):
                if 'google' not in page:
                    u = urlparse(page[7:])
                    yield (u.scheme + '://' + u.netloc)

if __name__ == "__main__":
    phrase = 'biura+architektoniczne+warszawa'
    webpage = google_web_page(phrase)
    links = get_links(webpage)

    for link in links:
        print(link)
        # dodanie linku do listy ( bazy danych )
        # tworzy bazę danych na podstawie wpisanej kategorii np. biura architektoniczne łódź
        # sprawdza czy dany link widnieje już w bazie danych oraz czy nie jest na black liście:
        # wikipedia, google, amazon, allegro , wp, onet itp.