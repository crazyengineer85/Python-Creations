import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        # Yeni bir personal access token oluşturmanız gerekebilir
        # https://github.com/settings/tokens adresinden
        self.token = "API_KEY"  # classic token veya fine-grained token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_user(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    
    def get_repository(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def create_repository(self, name):
        # Doğru endpoint: /user/repos (kullanıcı için repo oluştur)
        response = requests.post(
            self.api_url + '/user/repos',
            headers=self.headers,
            json={
                "name": name,
                "description": "This is your first repository",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
            }
        )
        return response.json()

github = Github()

while True:
    secim = input("1- Find User\n" 
                  "2- Get Repositories\n"
                  "3- Create Repository\n"
                  "4- Exit\nSeçim: ")
    
    if secim == "4":
        break
    elif secim == "1":
        print("\n" + "*" * 43 + "\n")
        username = input("enter username: ")
        x = github.get_user(username)
        if "message" in x and x["message"] == "Not Found":
            print("User not found!")
        else:
            print(f"name: {x.get('name', 'N/A')}\n"
                  f"public repo: {x.get('public_repos', 'N/A')}\n"
                  f"followers: {x.get('followers', 'N/A')}\n"
                  f"created_at: {x.get('created_at', 'N/A')}\n"
                  f"updated_at: {x.get('updated_at', 'N/A')}")
    elif secim == "2":
        print("\n" + "*" * 43 + "\n")
        username = input("enter username: ")
        x = github.get_repository(username)
        if isinstance(x, list):
            for repo in x:
                print(repo["name"])
        else:
            print("Error:", x.get("message", "Unknown error"))
    elif secim == "3":
        name = input("repository isim gir: ")
        x = github.create_repository(name)
        if "id" in x:  # Başarılı oluşturma
            print(f"Repository '{name}' successfully created!")
            print(f"URL: {x.get('html_url')}")
        else:
            print("Error creating repository:")
            print(x)
    else:
        print("Düzgün seç.....")
    
    print("\n" + "*" * 43 + "\n")