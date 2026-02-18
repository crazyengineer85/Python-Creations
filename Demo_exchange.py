import requests



api_key = "18cf31f72fd2e23a9e9407fe"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz turu: ") #USD
alinan_doviz = input("alınan döviz turu: ") #TRY
miktar = input (f"nekadar {bozulan_doviz} usd bozdurmak istiyorsun: ")




sonuc = requests.get(api_url + bozulan_doviz)
print (sonuc)
