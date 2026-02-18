# key-value şeklinde çalışır
# sehir = ['kocaeli', 'istanbul']
# plaka = [41, 34]

# eski usül:

# print(plaka[sehir.index('kocaeli')])
plaka = {'kocaeli': 41,
         'istanbul':34,
         'Izmir': 35
        }
print(plaka['istanbul'])
print(plaka['Izmir'])
print(plaka['istanbul'],plaka['Izmir'])
