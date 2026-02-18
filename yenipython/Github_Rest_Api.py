import requests




class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "API_KEY"

    
    def get_user(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json() # json.loads()yerine kullanılır json import etmeye gerek yok
    def get_repository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def create_repository(self, name):
        response = requests.post(self.api_url+'/users/repos?access_token='+self.token, json={
            "name": name,
            "description": "This is your first repository",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
github = Github()







while True:
    secim = input("1- Find User\n" 
    "2- Get Repositories\n"
    "3- Create Repositories\n"
    "4- Exit\nSeçim: "
    )
    if secim == "4":
        break
    elif secim== "1":
        print("\n*******************************************\n")
        username = input("enter username: ")
        x = github.get_user(username)
        print(f"name: {x["name"]}\npublic repo: {x["public_repos"]}\nfollowers: {x["followers"]}\ncreated_at: {x["created_at"]}\nupdated_at: {x["updated_at"]}")
    elif secim== "2":
        print("\n*******************************************\n")
        username = input("enter username: ")
        x = github.get_repository(username)
        for repo in x:
            print(repo["name"])

    elif secim== "3":
        name = input("repository isim gir: ")
        x = github.create_repository(name)
        print(x)
    else:
        print ("Düzgün seç.....")
    print("\n*******************************************\n")