import requests
from bs4 import BeautifulSoup


base_url = "https://www.imdb.com/list/ls023154907/"


headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"

}


butun_filmler = []
for page in range(1,3):
    url =f"{base_url}?page{page}"
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")
# html = requests.get(url, headers=headers).content
# print(html) # tüm html'i getirir
# soup = BeautifulSoup(html, "html.parser")
# liste = soup.find("ul",{"class":"ipc-metadata-list"}) # ilk <ul>'yi çeker liste değil
# liste = soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",{"class":"ipc-metadata-list-summary-item"}) # li liste olarak dondurur
liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li") # sadece bir tane <li>
for item in liste:
    # print(item)
    filmadi = item.find("h3", {"class":"ipc-title__text"}).text
    butun_filmler.append(filmadi)

print(len(butun_filmler))
for film in butun_filmler:
    print(film)