import math

def bos_fonksiyon():
    pass #henuz kodu yazilmamis fonksiyon (cppdeki prototip)

print(bos_fonksiyon())

def ekranaYazdir(string):
    print(string) #string argumani ekrana


ekranaYazdir("Gunaydin") #fonksiyon cagirilir

def ekranaYazdir2(str1, str2):
    print(str1, str2) #anahtar kelimeli arguman


ekranaYazdir2("selam", "beyza")

def kimNerde(ad= "Deniz", kent= "Istanbul"): #varsayilan arguman
    print("Adi:", ad)
    print("Yasadigi sehir: ", kent)
    print("-" * 30)

kimNerde("Halil", "Kesan")
kimNerde(ad = "Ahmet" )
kimNerde(kent = "Bursa")

def fonksiyon(ad, kent, *ozellik): #argumanin sayisi onceden belli degil
    #ad, kent ve kisisel ozellikleri ekrana basar
    print("Adi: ", ad)
    print("Yasadigi sehir: ", kent)
    ozel = ""
    for oz in ozellik:
        ozel = ozel + " " + oz
    print("Ozellikler: ", ozel)
    print("-"* 50)

fonksiyon("Hale", "Antalya", "Esmer", "Siyah", "Kısa")
fonksiyon("Jale", "İzmir", "Uzun")
fonksiyon("Lale", "İstanbul")

topla = lambda arg1, arg2: arg1 + arg2 #kucuk boyutlu fonksiyonlar icin kullanilir. lambda fonksiyonlari local ve global degiskenlere erisemzler.
carp = lambda arg1, arg2, arg3: arg1 * arg2 * arg3
hipotenus = lambda  kenar1, kenar2: math.sqrt(kenar1**2+kenar2**2)

print("12 + 27= ", topla(12, 27))
print("11 * 13 * 17= ", carp(11, 13, 17))

print("Kısa kenari 5, uzun kenari 12 olan ucgenin hipotenusu= ", hipotenus(5,12))
print("-"*50)
s = " Fonksiyonun disinda"

def funcAna():
    s1 = "s1 fonkisyonun icinde" #local degisken, sadece tanimli oldugu fonksiyonların ve o fonksiyona ait alt fonkisyonlarda tanimlidir
    print("funcAna fonskiyonun ici")
    def funcAlt():
        s2 = "funcAlt fonksiyonun ici" #local degisken
        print("funcAlt s= ", s)
        print("funcAlt s1= ", s1)
        print("funcAlt s2= ", s2)
        print("-"*50)
    funcAlt()
    print("funcAna s= ", s)
    print("funcAna s1= ", s1)
    # print("funcAna s2=  ", s2) #bu satir hata verir

funcAna()
print("funcAlt s=  ", s)
# print("funcAlt s1=  ", s1) #bu satir hata verir
# print("funcAlt s2=  ", s2) #bu satir hata verir

s = " Fonksiyonun disinda"
def funcAna2():
    global s1
    s1 = "s1 fonkisyonun icinde" #global degisken, kodun her yerinden erisim saglanabilir.
    print("funcAna fonskiyonun ici")
    def funcAlt2():
        global s2 #global degisken
        s2 = "funcAlt fonksiyonun ici"
        print("funcAlt s= ", s)
        print("funcAlt s1= ", s1)
        print("funcAlt s2= ", s2)
        print("-"*50)
    funcAlt2()
    print("funcAna s= ", s)
    print("funcAna s1= ", s1)
    print("funcAna s2=  ", s2)

funcAna2()
print("funcAlt s=  ", s)
print("funcAlt s1=  ", s1)
print("funcAlt s2=  ", s2)



