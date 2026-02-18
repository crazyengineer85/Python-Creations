hesapA ={
    'ad': 'Yekta Duran',
    'hesapno': '12345',
    'bakiye': 5000,
    'ekhesap': 8000
}

def paracek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>=miktar):

        print(f"paranızı çekiniz, {hesap['bakiye']-miktar} TL ana paranız kaldı, esnek hesabınızda da {hesap['ekhesap']} TL var.")




x = int (input("Çekeceğiniz para miktarını giriniz: "))
paracek(hesapA, x)