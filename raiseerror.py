
def pswcheck(psw):
    import re
    if len(psw)<8:
        raise Exception("en az 8 karakter içermeli")
    elif not re.search("[a-z]",psw):
        raise Exception("en az bir tane küçük harf içerecek")
    elif not re.search("[A-Z]",psw):
        raise Exception("en az bir tane büyük harf içerecek")
    elif not re.search("[0-9]",psw):
        raise Exception("en az bir tane rakam içerecek")
    elif not re.search(r"[!'^+%&/()=?*-]",psw):
        raise Exception("en az bir tane alpha numerik harf içerecek")
    elif re.search("\s",psw):
        raise Exception("boşluk karakteri içermeyecek")
    

while True:
    try:
        x = input("password gir: ")
        pswcheck(x)
    except Exception as e:
        print("passwsord'ü yanlış girdiniz: ", e)
    else:
        print("adam gibi girdiniz.....")
        break
    finally:
        print("validation tamam.....")














# while True:
#     try:
#         x = int (input("x: "))
#         y = int (input("y: "))
#         print(x/y)
#     except Exception as e:
#         print(" x ve y'yi girerken tam sayı olarak girin!....", e)
#         c  = c + 1
#         if c==3:
#             print("hakkın bitti mal oğlan:)")
#             break
#     else:
#         break




#     finally:
#         print("try except çalıştı....")