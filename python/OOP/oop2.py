import module 

class Person:

    def __init__(self, fistName, lastName, age):
        self.fn = fistName
        self.ln = lastName
        self.a = age


person1 = Person("Beyza Nur", "Kaya", 22)
print(person1.fn, person1.ln, person1.a)


class Worker(Person):

    def __init__(self, salary):
        self.slr = salary


class Customer(Person):

    def __init__(self, creditCard):
        self.cc = creditCard


ahmet = Worker(10)
