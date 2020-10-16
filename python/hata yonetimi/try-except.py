
try:
    sayi = int(input("Sayi giriniz: ")) #bu satiri isleme koy

except ValueError: #hata alirsa ne olsun
    print("Tip uyusmazligi, lütfen sayi giriniz.")
except ZeroDivisionError:
    print("Payda sifir olamaz.")
except:
    print("Bir hata olustu")

print("Bitti")

liste = [1,2,3]
try:
    print(liste[3])
except Exception as e:
    print("Hata:", e)

try:
    print(1/0)
except Exception as e:
    print("Hata:", e)
