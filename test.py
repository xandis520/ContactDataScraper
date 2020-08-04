from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

# Próba otworzenia linku (wyskakują błędy, jeżeli link nie istnieje
try:
    html = urlopen("http://adrian-portfolio.site/portfolio/")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found")
else:
    print("It worked")

# web_page = html.read()

bsObj = BeautifulSoup(html, 'lxml')
media_link = bsObj.find_all('a', {"class": "media-link"})
test = bsObj.find_all({"h1", "h2", "h3", "h4", "h5", "h6"})
test = bsObj.find_all("span", {"class": {"green", "red"}})
# Wyszukiwanie po frazie w tekście
test = bsObj.find_all(text="made")
# Wyszukiwanie po id (oba przykłady wywołują to samo)
test = bsObj.find_all(id="text")
test = bsObj.find_all("", {"id": "text"})
# Wyszukiwanie po klasie (oba przykłady wywołują to samo)
test = bsObj.find_all(class_="green")
test = bsObj.find_all("", {"class": "green"})
# Inne obiekty
test = bsObj.div.h1
test = bsObj.findAll("img")
# Dzieci obiektu
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)
# Sibling - nawigowanie do obiektów znajdujących się na tym samym poziomie w drzewie
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

for sibling in bsObj.find("table", {"id": "giftList"}).tr.previous_siblings:
    print(sibling)
# Parent
test = bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()

# Wyrażenia regularne - regex
# Email
# [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net|pl)
images = bsObj.findAll("img", {"src":re.compile(r"\.  \.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])









# for iteration, name in enumerate(media_link):
#     print(iteration+1, name.get_text().strip())
