class Employee: #parent

    def raisee(self):
        raise_rate = 0.1
        return print(100 + 100*raise_rate)

class CompEng(Employee): #subclass

    def raisee(self):
        raise_rate = 0.2
        return print(100 + 100*raise_rate)

class EEEng(Employee): #subclass

    def raisee(self):
        raise_rate = 0.05
        return print(100 + 100*raise_rate)

#parent class farkli classlarda kullanilmasi overriding ve polimorphism ile saglanir
e1 = Employee()
ce = CompEng()
eee = EEEng()

e1.raisee()
ce.raisee()
eee.raisee()