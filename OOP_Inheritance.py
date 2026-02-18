# Inheritance (Kalıtım): Class'ların birbirinden miras alması
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Person class'ı çalıştırıldı")
    def who_am_i(self):
        print("I'm a person")

    def eat(self):
        print("I'm eating")

class Student(Person):
    def __init__(self, fname, lname, snumber): # Personun variable'larını çağır
        self.studentnumber = snumber
        Person.__init__(self, fname, lname) # Personun variable'larını gönder
        print("Student class'ı çalıştırıldı")
        # *************override**************
    def who_am_i(self):
        print("I'm a student")
    def eat(self):
        print("I'm eating sandwich")
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) # Person.__init__(self, fname, lname) alternatifi
        self.teachername = fname
        self.teachersurname = lname
        self.teacherbranch = branch



# p1 = Person() 
#s1 = Student() # Student class'ı çalıştırılmadı pass var __init__ yok, sadece Person class'ından aldığı mirası çalıştırdı



p1 = Person('yekta', 'duran')
s1 = Student('barış', 'duran', '12345')
t1 = Teacher('yekta', 'duran', 'Maths')


print(f"adı: {p1.firstname}, soyadı: {p1.lastname}")
print(f"ad: {s1.firstname}, soyad: {s1.lastname}, y: {s1.studentnumber}")
print(f"ad: {t1.teachername}, soyad: {t1.teachersurname}, y: {t1.teacherbranch}")

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()