import math
a = 1
b = 2

print("a = ", a , "b = ", b)
if a>b:
    print(a, "degeri", b, "\'den buyuktur ")
if a<b:
    print(a, "degeri", b, "\'den kucuktur ")
if b>0:
    c = math.sqrt(4*a+b**2)
    print("(4*a+b**2)\'nin karekoku", c, "\'dir")


if a>b:
    print(a, "degeri", b, "\'den buyuktur ")
else:
    print("Ben de bilmiyorum.")

isimler = ["ali", "ahmet", "ayse", "beyza"]
for ad in isimler:
    if ad == "ali":
        print("Arkadasim", ad)
    elif ad == "ahmet":
        print("Arkadasim", ad)
    elif ad == "ayse":
        print("Arkadasim", ad)
    else:
        print("Seni tanimiyorum.")



