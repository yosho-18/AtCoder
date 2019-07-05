import requests
from bs4 import BeautifulSoup


class Scraping_Tennis(object):
    tennis_list = []
    tennis_factor = ["rank", "name", "country", "point"]
    r = requests.get("https://sportsnavi.ht.kyodo-d.jp/tennis/ranking/atp/point/")
    soup = BeautifulSoup(r.content, "html.parser")
    count = 0
    tennis_list = []
    for item in soup.find("table").find_all('td'):
        if count % 4 == 2:
            element = item.find_all('span')
            print(element[1].text)
            tennis_list[-1][tennis_factor[count % 4]] = element[1].text
            count += 1
            continue
        elif count % 4 == 0:
            tennis_list.append({})
        tennis_list[-1][tennis_factor[count % 4]] = item.text
        count += 1
    print(tennis_list)
