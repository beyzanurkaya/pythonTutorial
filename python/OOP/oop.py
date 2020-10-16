class Matematik:

    def __init__(self):
        print("Calisti...")

    def topla(self, sayi1, sayi2):
        return sayi1 + sayi2

    def cikar(self, sayi1, sayi2):
        return sayi1 - sayi2

    def carp(self, sayi1, sayi2):
        return sayi1 * sayi2

    def bol(self, sayi1, sayi2):
        return sayi1 / sayi2


matematik = Matematik() #matematik nesnesi olusturuldu
matematik2 = Matematik()
print("Toplam= ", matematik.topla(34,2))
print("Fark= ", matematik.cikar(34,2))
print("Carpim= ", matematik.carp(34,2))
print("Bolum= ", matematik.bol(34,2))

#--------------------------------------------------------------------------------------#


class Matematik2:

    def __init__(self, sy1, sy2): #selfin ici
        print("Calisti...")
        self.sayi1 = sy1
        self.sayi2 = sy2
    def topla(self):

        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

    def bol(self):
        return self.sayi1 / self.sayi2

print("---" * 10)
mat = Matematik2(34,2) #mat nesnesi olusturuldu
mat2 = Matematik2(90,3)
print("Toplam= ", mat.topla())
print("Fark= ", mat.cikar())
print("Carpim= ", mat2.carp())
print("Bolum= ", mat2.bol())