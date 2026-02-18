Yektahesap = {
    'ad': 'Yekta Duran',
    'hesapno': '132458',
    'bakiye': 5000,
    'ekhesap':5000
}

Barishesap = {
    'ad': 'Barış Yiğitcan Duran',
    'hesapno': '1324588',
    'bakiye': 8000,
    'ekhesap':8000
}

def paracek(hesap, miktar):
    print(f"Merhaba {hesap['ad']} ")
    if hesap['bakiye']>=miktar:
        print(f"paranızı alabilirsiniz, {(hesap['bakiye'])-miktar} TL ana paranız, {hesap['ekhesap']} TL ek hesabınız kaldı")
    else:
        toplam = hesap['bakiye']+hesap['ekhesap']

        if toplam>=miktar:
            kullan = input("ek hesabınızı kullanmak istiyor musunuz? (e/h)")
            if kullan=='e':
                print(f"paranızı alabilirsiniz,{toplam-miktar} TL ek hesap bakiyeniz kaldı")
            else:
                print(f"bakiyeniz {hesap['bakiye']} TL olup yetersizdir")
        else:
            print(f"toplam paranız çekmek itediğiniden az olduğundan bakiyeniz: {hesap['bakiye']} ve ek hesap bakiyeniz:{hesap['ekhesap']}")



paracek(Yektahesap,4000)