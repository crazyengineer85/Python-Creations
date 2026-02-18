hesapBaris = {

    'ad': 'Barış abi:)',
    'hesapno': '88888',
    'bakiye': 8000,
    'esnekhesap': 8000
}

def paracekbaris(hesap, cekilecek_para):
        
        
        if (hesap['bakiye']>= cekilecek_para):
                
             print(f"paranız çekiliyor, {hesap['bakiye'] - cekilecek_para} TL paranız kalmıştır, Esnek hesap Limitiniz: {hesap['esnekhesap']} TL'dir")
        else:
              toplam_para = hesap['bakiye'] + hesap['esnekhesap']
              x = input("Bakiyeniz yetersizdir, esnekhesap Limitinizi kullanmak istiyor musunuz? (e/h)")
              if x=='e':
                    if toplam_para>= cekilecek_para:
                          kalan_para = hesap['esnekhesap']-(cekilecek_para-hesap['bakiye'])
                          print(f"paranız çekiliyor anaparanız 0 TL kalmıştır, esnekhesap Limitiniz {kalan_para} TL kalmıştır")
                          q = int(input("çekmek istediğiniz miktarı girin: "))
                          if kalan_para>= q:
                                enson= kalan_para - q
                                print(f"hesabınızda {enson} TL para kalmıştır")
                          else:
                                print("çekilecek para yetersizdir")

                    else:
                          print("total paranız yetersizdir")  
              else:
                print ("anaparanız yetersizdir")

def parayatirbaris(hesap, yatirilacak_para):
      pass
                    
                    
                    
                    
              





giris_basarili = False

for _ in range(3):
     if not giris_basarili:
           y = input("Şifre giriniz: ")
           if y=="1993":
                 giris_basarili = True
                 print(f"Merhaba {hesapBaris['ad']}")
                 print(f"Hesabınızda {hesapBaris['bakiye']} TL vardır")
                 print(f"Esnek hesap Limitiniz: {hesapBaris['esnekhesap']} TL'dir")
                #  w= input("Para çekmek için 1'e, yatırmak için 2'ye basınız: ")
                #  if w == '1':
                 x = int(input("Çekeceğiniz miktarı giriniz: "))
                 paracekbaris(hesapBaris,x)
                #  elif w=='2':
                #        q = int(input("Yatıracağınız miktarı giriniz: "))
                #        parayatirbaris(hesapBaris,q)
                #  else:
                #        print("yanlış bir tuşa bastınız")
                 
           
          
           else:
                 print ("Şifre yanlış")
     
              
if not giris_basarili:
     print("hesabınız bloke olmuştur")
          
    
     
     
          
     




















# if y=="1993":
#     print(f"Merhaba {hesapBaris['ad']}")
#     print(f"Hesabınızda {hesapBaris['bakiye']} TL vardır")
#     print(f"Esnek hesap Limitiniz: {hesapBaris['esnekhesap']} TL'dir")
#     x = int(input("Çekeceğiniz miktarı giriniz: "))
#     paracekbaris(hesapBaris,x)

# else:
#     print ("Şifre yanlış")