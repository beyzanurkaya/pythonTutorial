#variables

a = 1 #degisken tanimlama
b = 4
s1 = "beyza nur"
s2 = " kaya"

s3 = s1 + s2
s4 = s1*3

#return kavrami

def topla1(num1, num2):
    toplam = num1 + num2 #2 sayinin toplamini bir degiskene ata ve o degiskeni dondur
    return toplam

def topla2(num1, num2):

    return num1 + num2 #dogrudan 2 sayinin toplamini dondur

print("5 + 7= ", topla1(5,7))
print("5 + 7= ", topla2(5,7))


print(s3)
print(s4)

ad = input("Adiniz: ") #kullanicidan girdi alma
print("Merhaba", ad)
sy1 = input("Birinci sayi= ")
sy2 = input("İkinci sayi= ")
print(sy1, "+", sy2, "= ", (int(sy1) + int(sy2)))



