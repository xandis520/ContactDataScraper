from bs4 import BeautifulSoup
import requests
from requests import ConnectionError
import re
from urllib.request import Request, urlopen


########################################################################
# GETTING PAGE CONTENT USING urllib.request
########################################################################
def get_web_page(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req.add_header('Accept-Encoding', 'utf-8')

    web_byte = urlopen(req).read()

    webpage = web_byte.decode('utf-8')

    return webpage


########################################################################
# GETTING PAGE CONTENT USING BEAUTIFULSOUP
########################################################################
def get_soup(url, parser='html.parser', user_agent='desktop'):
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

    ########################################################################
    # SEARCHING ALL INTERNAL LINKS IN GIVEN PAGE URL
    ########################################################################
    def get_internal_links(self):
        for link in self.soup.find_all("a"):
            if 'href' in link.attrs:
                if self.url in link.attrs['href']:
                    internal_url = link.attrs['href']
                    yield internal_url
                elif link.attrs['href'].startswith('/'):
                    internal_url = self.url + link.attrs['href']
                    yield internal_url


########################################################################
# FILTERING ALL PAGES TO GET ONLY CONTACT PAGES
########################################################################
def get_contact_pages(internal_links, words_list=None):
    words_list = ['kontakt', 'contact']
    contact_pages = [link for word in words_list for link in internal_links if word in link]
    # Removing duplicates from list
    contact_pages = list(dict.fromkeys(contact_pages))
    return contact_pages


########################################################################
# GETTING CONTACT DATA FROM PAGE URL
########################################################################
class ContactData:
    def __init__(self, url, parser='html.parser', user_agent='desktop'):
        #######################################################################
        # GETTING SOUP OR WEBPAGE
        #######################################################################
        self.page = str(get_soup(url=url, parser=parser, user_agent=user_agent))
        # self.webpage = get_web_page(url)
        # self.page = self.webpage

    def get_contact_data(self, settings):
        #######################################################################
        # PHONE
        #######################################################################
        if settings["phone"] == 'True':
            phone = self.get_phone()

        #######################################################################
        # Nip
        #######################################################################
        if settings["nip"] == 'True':
            nip = self.get_nip()

        #######################################################################
        # EMAILS
        #######################################################################
        if settings["email"] == 'True':
            email = self.get_email()

        #######################################################################
        # RETURN DATA
        #######################################################################
        data = {
            "phone": phone,
            "email": email,
            "street": None,
            "street_number": None,
            "apartment": None,
            "city": None,
            "postal_code": None,
            "nip": nip,
            "regon": None
        }

        return data

    def get_phone(self):
        r_phone = re.compile(r'\b\d{3}[-\s\*\.]?\d{3}[-\s\*\.]?\d{3}\b')
        # r_landline_phone = re.compile(r'\+?48[-\s\*\.]+\d{2,3}[-\s\*\.]?\d{2,3}[-\s\*\.]?\d{2}[-\s\*\.]?\d{2}')
        # r = re.compile(r'\b\d{3}[-\s\*\.]?\d{3}[-\s\*\.]?\d{3}\b')
        # phone_results = r_landline_phone.finditer(soup)
        phone_results = r_phone.finditer(self.page)
        phone = []
        for number in phone_results:
            number = number.group()
            if number not in phone:
                phone.append(number)
        return phone

    def get_nip(self):
        r_nip = re.compile(r'\b\d{3}[-\s\*\.]?\d{3}[-\s\*\.]?\d{2}[-\s\*\.]?\d{2}\b')
        nip_results = r_nip.finditer(self.page)
        nip = []
        for number in nip_results:
            number = number.group()
            if number not in nip:
                nip.append(number)
        return nip

    def get_email(self):
        r_email = re.compile(r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''')
        email_results = r_email.finditer(self.page)
        emails = []
        for email in email_results:
            email = email.group()
            if email not in emails:
                emails.append(email)
        return emails

    def get_adress(self):
        pass

    def get_city(self):
        pass

    def get_postal_code(self):
        pass

    def get_regon(self):
        pass
