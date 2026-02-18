from datetime import date
import calendar

# Doğum tarihi bilgileri (burayı değiştirebilirsiniz)
print("Doğum tarihinizi girin:")
dogum_gunu = int(input("Gün (1-31): "))
dogum_ayi = int(input("Ay (1-12): "))
dogum_yili = int(input("Yıl: "))


# Bugünün tarihini al
bugun = date.today()

# Yaş hesaplama
yas_yil = bugun.year - dogum_yili
yas_ay = bugun.month - dogum_ayi
yas_gun = bugun.day - dogum_gunu

# Gün negatifse düzelt
if yas_gun < 0:
    yas_ay = yas_ay - 1  # Bir ay eksilt
    
    # Önceki ayın tarihini oluştur
    if bugun.month == 1:
        onceki_ay_yil = bugun.year - 1
        onceki_ay_ay = 12
    else:
        onceki_ay_yil = bugun.year
        onceki_ay_ay = bugun.month - 1
    
    # Önceki ayın gün sayısını bul
    gun_sayisi = calendar.monthrange(onceki_ay_yil, onceki_ay_ay)[1]
    yas_gun = yas_gun + gun_sayisi

# Ay negatifse düzelt
if yas_ay < 0:
    yas_yil = yas_yil - 1  # Bir yıl eksilt
    yas_ay = yas_ay + 12   # 12 ay ekle

# Sonucu yazdır
print(f"Doğum tarihiniz: {dogum_gunu:02d}/{dogum_ayi:02d}/{dogum_yili}")
print(f"Bugünün tarihi: {bugun.day:02d}/{bugun.month:02d}/{bugun.year}")
print(f"Yaşınız: {yas_yil} yıl, {yas_ay} ay, {yas_gun} gün")