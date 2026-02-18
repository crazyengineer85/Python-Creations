import requests
import json



api_key = "API_KEY"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz turu: ") #USD
alinan_doviz = input("alınan döviz turu: ") #TRY
miktar = int(input (f"nekadar {bozulan_doviz} usd bozdurmak istiyorsun: "))
# <Response [200]> geliyor, bu json datasını python'da okunabilir bir hale çevireceğiz




sonuc = requests.get(api_url + bozulan_doviz)

# print (sonuc)
# print(sonuc.text)
sonuc_json = json.loads(sonuc.text) # JSON.LOADS() JSON -> PYTHON STRING
# print(sonuc_json["conversion_rates"])
# print(sonuc_json["conversion_rates"][alinan_doviz])
print(f"1 {bozulan_doviz} = {sonuc_json["conversion_rates"][alinan_doviz]} {alinan_doviz}")
print(f"{miktar} {bozulan_doviz} = {miktar*sonuc_json["conversion_rates"][alinan_doviz]} {alinan_doviz}")