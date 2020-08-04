from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
phrase = input("Podaj szukaną frazę:").strip().replace(" ", "+")
google_html = 'https://www.google.com/search?q='
url = google_html + phrase

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')

# print(webpage)

bsObj = BeautifulSoup(webpage, 'html.parser')
link1 = bsObj.find("div", {"class": "r"})
# for child in link1:
#     print(child)
print(bsObj)

# with open(r'strona.html', 'w') as strona:
#     strona.write(bsObj.find_all())