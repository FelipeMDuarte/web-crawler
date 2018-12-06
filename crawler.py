import requests
from bs4 import BeautifulSoup

def run():
    base_url = 'https://www.epocacosmeticos.com.br/produtos'
    url = base_url
    url_visited = list()
    while(1):
        url_visited.append(url)
        print(url_visited)
        response = requests.get(url)
        # print(response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.get_text())

        type = soup.find("meta", property="og:type")
        if type and type.get("content") == "og:product":
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            if 'productName'in soup.get_text():
                print("#######@###############################################################")

        for link in soup.find_all("a", href=True):
            print("@@@@@@", link)
            url = link.get("href")
            print("%%%%%%%%%", url)
            if url not in url_visited and base_url in url:
                pass
            else:
                break;
run()
