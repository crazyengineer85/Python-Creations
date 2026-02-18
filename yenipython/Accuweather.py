import requests



class Weather:
    def __init__(self):
        self.api_url = "https://dataservice.accuweather.com"
        self.api_token = "API_KEY"
    def get_top_cities(self, count = 50):
        
        api_token = {"apikey": self.api_token}
        response = requests.get(f"{self.api_url}/locations/v1/topcities/{count}", params=api_token)
        if response.status_code== 200:
            return response.json()
        else:
            print("Error:", response.status_code, response.text)
            return None
    def get_current_weather(self, location_key):
        url = f"{self.api_url}/locations/v1/{location_key}"
        params = {
        "apikey": self.api_token
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code, response.text)
            return None
    

weather8 = Weather()

while True: 
    secim = input("1- Popular Cities\n"
    "2- Search City:\n"
    "3- Exit\nChoice: "
    )
    if secim == "3":
        break
    else:
        if secim == "1":
            cities = weather8.get_top_cities(10)
            if cities:
                for i in cities:
                    city_name = i["EnglishName"]
                    key = i["Key"]


                    weather = weather8.get_current_weather(key)
                    if weather:
                        w = weather[0]
                    print(w["WeatherText"], "-", w["Temperature"]["Metric"]["Value"], "°C")
        if secim == "2":
            pass


    

