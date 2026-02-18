import requests
from bs4 import BeautifulSoup



base_url = "https://www.migros.ch/en/category/fruits-vegetables/vegetables"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
all_vegetables = []




for page in range(1,3):
    url = f"{base_url}?page={page}"
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    liste = soup.find("ul", {"class":"subcat"}).find_all("li")
    # ul = soup.find("ul", class_="subcat")
    # print(ul)
    # print(soup.prettify()[:2000])
    for item in liste:
        vegetable_name = item.find("span",{"class":"desc"}).text
        all_vegetables.append(vegetable_name)
print(len(all_vegetables))
for vegetable in all_vegetables:
    print(vegetable)