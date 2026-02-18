from school import School
def test_add_student():
    school = School()
    school.add("Yekta")
    school.count()
    assert school.count()==1

    # normalinde yapacağımız işlem
    # if school.count()!=1:
    #     raise Exception
    # Bunun yerine python da "assert" keyword'ünü kullanırız
    # assert school.count()==1 i burada 1 mi değil mi diye bakıyor, hata verecek