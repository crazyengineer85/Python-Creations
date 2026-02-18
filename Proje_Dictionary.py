arabalar = {}
marka = input ('araba markası : ')
model = input ('araba modeli : ')
yakit = input ('araba yakıtı : ')
tipi = input ('araba tipi : ')

arabalar.update ({
marka:{
'model':model,
'yakıt':yakit,
'tipi':tipi
}})



marka = input ('araba markası : ')
model = input ('araba modeli : ')
yakit = input ('araba yakıtı : ')
tipi = input ('araba tipi : ')

arabalar.update ({
marka:{
'model':model,
'yakıt':yakit,
'tipi':tipi
}})




marka = input ('araba markası : ')
model = input ('araba modeli : ')
yakit = input ('araba yakıtı : ')
tipi = input ('araba tipi : ')

arabalar.update ({
marka: {
'model':model,
'yakıt':yakit,
'tipi':tipi
}})


# print(arabalar)

araba_marka = input ("araba marka: ")
x = arabalar[araba_marka]
print(x)
