# themoviedb.org => film dizi arşivi
# buradaki apiyi kullan
# anahtar kelimeye göre ara
# enpopüler film listesi
# vizyondaki film listesi


import requests

class MovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "API_KEY"
        
        # https://api.themoviedb.org/3/movie/550?api_key=API_KEY => Burada 550 filmin ID bilgisi
    def get_popular(self):
        respose = requests.get(f"{self.api_url}/movie/top_rated?api_key={self.api_key}&language=en-US&page=1")
        return respose.json()
    def get_search_results(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
movie = MovieDb()
while True:
    secim = input("1- Popular Movies\n"
    "2- Search Movies:\n"
    "3- Exit\nSeçim: "
    )
    if secim == "3":
        break
    else:
        if secim =="1":
            count = 0
            x = movie.get_popular()
            for i in x['results']:
                count += 1
                print(f"{count} - {i['original_title']}")
                # print(i) # tüm gelen movieler ekrana yazdırılır
                
        if secim =="2":
            keyword = input("search: ")
            x = movie.get_search_results(keyword)
            for i in x['results']:
                print(f"film Id = {i[str('id')]} : film Adı: {i['name']}") # tüm gelen movieler ekrana yazdırılır               