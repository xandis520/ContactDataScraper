# Skrypt przeszukuje stronę w poszukiwaniu danych kontaktowych i innych
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from requests import ConnectionError
import re
from urllib.request import Request, urlopen


def get_web_page(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req.add_header('Accept-Encoding', 'utf-8')

    web_byte = urlopen(req).read()

    webpage = web_byte.decode('utf-8')

    return webpage


def get_soup(url, parser='html.parser', user_agent='desktop'):
    # Parser = 'lxml' or 'html.parser'
    # user_agent = desktop, mobile
    USER_AGENT = {
        "desktop": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0",
        "mobile": "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    }
    USER_AGENT = USER_AGENT[user_agent]
    headers = {"user-agent": USER_AGENT}

    try:
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, parser)
            return soup
    except ConnectionError:
        raise ConnectionError(
            'Probably you have used incorrect link!')
    except ImportError:
        raise ImportError('You need to have installed bs4, requests, html.parser and lxml')


class CompanyDataSearch:
    def __init__(self, url=None, soup=None, parser='html.parser', user_agent='desktop'):
        self.url = url
        if url:
            self.soup = get_soup(url=url, parser=parser, user_agent=user_agent)
        elif soup:
            self.soup = soup
        else:
            raise ValueError('You have to define url or soup')

    def get_internal_links(self):
        for link in self.soup.find_all("a"):
            if 'href' in link.attrs:
                if self.url in link.attrs['href']:
                    internal_url = link.attrs['href']
                    yield internal_url
                elif link.attrs['href'].startswith('/'):
                    internal_url = self.url + link.attrs['href']
                    yield internal_url


def get_contact_pages(internal_links):
    words_list = ['kontakt', 'contact']
    contact_pages = [link for word in words_list for link in internal_links if word in link]
    # Removing duplicates from list
    contact_pages = list(dict.fromkeys(contact_pages))
    return contact_pages


def get_contact_data(url, parser, user_agent):
    # Optional soup or webpage
    soup = str(get_soup(url=url, parser=parser, user_agent=user_agent))
    # webpage = get_web_page(url)

    # Phone
    r_phone = re.compile(r'\b\d{3}[-\s\*\.]?\d{3}[-\s\*\.]?\d{3}\b') # Znajduje też numery, które poprzedzone są znakiem '/'. Trzeba to poprawić.
    # r_landline_phone = re.compile(r'\+?48[-\s\*\.]+\d{2,3}[-\s\*\.]?\d{2,3}[-\s\*\.]?\d{2}[-\s\*\.]?\d{2}')
    # r = re.compile(r'\b\d{3}[-\s\*\.]?\d{3}[-\s\*\.]?\d{3}\b')
    # phone_results = r_landline_phone.finditer(soup)
    phone_results = r_phone.finditer(soup)
    phone = []
    for number in phone_results:
        number = number.group()
        if number not in phone:
            phone.append(number)

    # Nip
    r_nip = re.compile(r'\b\d{3}[-\s\*\.]?\d{3}[-\s\*\.]?\d{2}[-\s\*\.]?\d{2}\b')
    nip_results = r_nip.finditer(soup)
    nip = []
    for number in nip_results:
        number = number.group()
        if number not in nip:
            nip.append(number)

    data = {
        "phone": phone,
        "email": None,
        "street": None,
        "street_number": None,
        "apartment": None,
        "city": None,
        "postal_code": None,
        "nip": nip,
        "regon": None
    }

    return data


if __name__ == '__main__':
    page_url = 'http://www.dsgn.pl/'
    # page_url = 'http://janderkabza.pl/kontakt/'
    # page_url = 'http://www.archdesign.pl/architekt_warszawa/kontakt'
    page = CompanyDataSearch(url=page_url)
    internal_links = page.get_internal_links()
    # contact_page = get_contact_pages(internal_links)
    contact_data = get_contact_data(page_url)
    # print(contact_data)
    for key, value in contact_data.items():
        # print(re.sub('\D', '', result.group()))
        # print(''.join(filter(str.isdigit, result.group())))
        print(key+":", value)

    for result in internal_links:
        print(result)

    # print(get_web_page('https://www.google.pl/search?biuro+architektoniczne'))