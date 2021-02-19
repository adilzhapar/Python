class Person:
    def __init__(self, fname, sname):
        self.firstname = fname
        self.secondname = sname

class Car(Person):
    def __init__(self, fname, sname, model):
        self.model = model
        Person.__init__(self, fname, sname)

p1 = Person("Adil", "Zhapar")
print(p1.firstname)
print(p1.secondname)
c1 = Car("Adil", "Zhapar", "BMW")
print(c1.firstname, c1.secondname, c1.model)