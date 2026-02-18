x = int (input('sayı: '))
asaLmi =True
if x==1:
    asaLmi = False
for i in range(2,x):
    if x%i==0:
        asaLmi = False
        break
if asaLmi:
    print('asal')
else:
    print('asal değil')