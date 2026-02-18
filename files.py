"""
Docstring for files


Dosya açmak-oluşturmak => open() fonksiyonu
Kullanımı => open(dosya adı(dosyanın adresi, dosya erişim modu))
dosya erişim modu = > Dosyaya hangi amaçla açtığımız belirtir (w/a/x/r)







w (write) => yazma, 
1- Dosyayı konumda yeni oluşturur,
2- cursor başta çalışacağından her fonk çalıştırıldığında eskisini siler yenisini yazar
# file = open("newfile.txt","w") ayni dizinde
# file = open("C:/users/YEKTA/Desktop/newfile.txt", "w") farkli dizinde
# file = open("newfile.txt", "w", encoding="utf-8")
# file.write("Barış BYE BYE!")
# file.close()
a (append) => ekleme, 
1- Dosyayı konumda yoksa oluşturur
2- cursor yazılanın sonunda çalışacağından her fonk çalıştırıldığında eskisinin bitimine yenisini yazar
file = open("newfile.txt", "a", encoding="utf-8")
file.write("Barış BYE BYE!")
file.write("\nYekta BYE BYE!")
file.close()
x (create) => oluşturma, Dosya konumda zaten varsa hata verir
file = open("newfile2.txt", "x", encoding="utf-8")
file.close()
r (read) => okuma, varsayılan, Dosya konumda yoksa hata verir

"""














