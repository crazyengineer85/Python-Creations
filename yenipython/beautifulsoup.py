html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WEB SAYFAM</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>
    <p>Bu kurs çok süper</p>
    <div class="group1">
    <h2>Programlama</h2>
    <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
        <li>Menu 5</li>

    </ul>
    </div>
   <div class="group2">
    <h2>Modüller</h2>
    <ul>
      <li>Menu 1</li>
        <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
      <li>Menu 5</li>

    </ul>
    </div>
    <div class="group3">
    <h2>Döngüler</h2>
    <ul>
        <li>Menu 1</li>   <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
        <li>Menu 5</li>

    </ul>
    </div>
    <div class="group4">
    <h2>Koşullar</h2>
    <ul>
       <li>Menu 1</li>
        <li>Menu 2</li>
       <li>Menu 3</li>
        <li>Menu 4</li>
        <li>Menu 5</li>

    </ul>
    </div>
    <div class="group5">
    <h2>Dosya Yönetimi</h2>
    <ul>
    <li>Menu 1</li>
        <li>Menu 2</li>
       <li>Menu 3</li>
     <li>Menu 4</li>
       <li>Menu 5</li>

   </ul>
    <img src="caddyyy.jpg" alt="" width="200px" height="200px">
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/elsie" id="link2">Elsie</a>
    <a class="sister" href="http://example.com/elsie" id="link3">Elsie</a>
    <a class="sister" href="http://example.com/elsie" id="link4">Elsie</a>
    <a class="sister" href="http://example.com/tillie" id="link5">Elsie</a>
</body>
</html>





"""




from bs4 import BeautifulSoup




soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify()) # burası html'yi düzenler
# print(soup.title) # etiketle birlikte verir
# print(soup.title.name) # yalnız etiketi verir
# print(soup.title.string) # Ana başlık
# print(soup.title.parent.name)
# print(soup.p.string)
# print(soup.p)
# print(soup.a["class"])
# # print(soup.find_all('a'))
# print(soup.find(id='link5').get('href'))
# # print(soup.get_text())
# print(soup.img.get('src'))

# x = soup.div.findChildren()
# x = soup.div
# x = soup.div.find_next_siblings() # bütün kardeşler
x = soup.div.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_previous_sibling()
x =soup.find_all('a')
for i in x:
    print(i["href"],i["id"])
# print(x)