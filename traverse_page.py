# Skrypt przeszukuje stronę w poszukiwaniu danych kontaktowych i innych
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from requests import ConnectionError


class CompanyDataSearch:
    def __init__(self, url=None):
        self.url = url

    def get_soup(self):
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        # MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
        headers = {"user-agent": USER_AGENT}
        try:
            req = requests.get(self.url, headers=headers)
            if req.status_code == 200:
                soup = BeautifulSoup(req.content, "html.parser")
                return soup
        except ConnectionError:
            raise ConnectionError(
                'Probably you have used incorrect link!')

    def get_internal_links(self, bs_obj):
        for link in bs_obj.find_all("a"):
            if 'href' in link.attrs:
                if page_url in link.attrs['href']:
                    internal_url = link.attrs['href']
                    yield internal_url
                elif link.attrs['href'].startswith('/'):
                    internal_url = page_url + link.attrs['href']
                    yield internal_url


page_url = 'http://www.archdesign.pl'
page = CompanyDataSearch(page_url)
soup = page.get_soup()
internal_links = page.get_internal_links(soup)
for link in internal_links:
    print(link)
