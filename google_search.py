# 1. Wprowadzić opcję ustawiawiania user_agenta
# 2.
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup
import requests
from requests import ConnectionError


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
                    yield urlunparse((page_url.scheme, page_url.netloc, page_url.path, '', '', ''))

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
