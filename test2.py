from bs4 import BeautifulSoup
import requests
import urllib

query = 'biura+architektoniczne+warszawa&ei=E4swX6rpAZaO1fAPxYGjuAM&start=90&sa=N&ved=2ahUKEwjqvuywp4_rAhUWRxUIHcXACDcQ8tMDegQIDRBJ'
# query = "biura architektoniczne warszawa"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

pages_dict = dict()
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")

pages_links = soup.findAll("a", {"class": "fl"})
for page_link in pages_links:
    try:
        key_value = str(page_link['aria-label'])
        if key_value not in pages_dict.keys():
            pages_dict[key_value] = page_link['href']
    except ValueError:
        pass
    except KeyError:
        pass

print('dict:', pages_dict)
# print(pages_dict['Page 3'])

# with open("output1.html", "w", encoding='utf-8') as file:
#     file.write(str(soup))

# results = []
# for g in soup.find_all('div', class_='r'):
#     anchors = g.find_all('a')
#     if anchors:
#         link = anchors[0]['href']
#         title = g.find('h3').text
#         item = {
#             "title": title,
#             "link": link
#         }
#         results.append(item)
# print(results)
