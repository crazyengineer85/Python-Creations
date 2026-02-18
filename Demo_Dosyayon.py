def sinavortalama(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    isim =  liste[0]
    score = liste[1].split(',')
    vize1 = int(score[0])
    vize2 = int(score[1])
    final = int(score[2])

    ortalama =  (((vize1+vize2)/2)*0.6) + (final*0.4)

    if ortalama>=90 and ortalama <=100:
        harf = "AA"
    else:
        harf = "CC"
    return isim + ": "+ harf + "\n"
    








def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(sinavortalama(satir))


def not_gir():
    ad    = input("ad: ")
    soyad = input("soyad: ")
    vize1 = input("vize1: ")
    vize2 = input("vize2: ")
    final = input("final: ")




    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+vize1+","+vize2+","+final+"\n")

    

def not_kayit_et():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(sinavortalama(i))
    with open("sinav_sonuclari.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)




while True:
    islem = input(
        "1- Notları oku: " 
        "\n2- Not gir: "
        "\n3- Not kayıt et: "
        "\n4- Çık:\n"
    
    )
    if islem == "1":
        notlari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kayit_et()
    elif islem == "4":
        break