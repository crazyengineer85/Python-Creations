'''
öğrenciler = {

'150':{
'ad': 'Ali'
'soyad':'Yılmaz'
'telefon': '552 000 00 02
},

'180':{
'ad': 'Can'
'soyad':'Korkmaz'
'telefon': '552 000 00 04
},
'200':{
'ad': 'Volkan'
'soyad':'Yükselen'
'telefon': '552 000 00 08
}
}

'''

# 1- Yukarıdaki bilgiler kullanıcıdan al
# 1. Yol
ogrenciler = {}
numara = input('ö. no:')
ad = input('ö. ad:')
tlf = input('ö. tlf:')


# 1.Yol
# ogrenciler[numara] = {'ad': ad,
#                       'tlf': tlf}
# 2.Yol
ogrenciler.update({
    numara: {

        'ad': ad,
        'tlf':tlf
    }
})
print(ogrenciler)
# 2- Öğrenci numarası bilgisi

ogrno = input('ö. no: ')
ogr = ogrenciler[ogrno]
print (ogr)