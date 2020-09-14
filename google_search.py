from urllib.parse import urlparse, urlunparse
from traverse_page import get_soup


class GoogleSearch:
    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase = self.phrase.replace(' ', '+')

        self.url = f"https://google.pl/search?q={self.phrase}"

    def get_soup(self, url=None, parser='html.parser', user_agent='desktop'):
        # Parser = 'lxml' or 'html.parser'
        # user_agent = desktop, mobile
        if url is None:
            url = self.url

        return get_soup(url=url, parser=parser, user_agent=user_agent)

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
