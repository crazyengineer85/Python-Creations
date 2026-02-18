from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

products = soup.select("ul.subcat li.item")

all_vegetables = []

for product in products:
    # Ürün adı
    name_tag = product.select_one("span[data-testid^='product-name']")
    name = name_tag.text.strip() if name_tag else "NO NAME"

    # Fiyat
    price_tag = product.select_one("span[data-testid='current-price']")
    price = price_tag.text.strip() if price_tag else "NO PRICE"

    all_vegetables.append((name, price))

print(len(all_vegetables))
for v in all_vegetables:
    print(v)