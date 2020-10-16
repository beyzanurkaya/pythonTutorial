
liste = [1, 3, 'a', 7, 'b', 5]

sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

 #Butun istisnalar hatadan kaynakli degildir. Akisi daha rahat denetlemek icin kendimiz de bir istisna tetikleyebiliriz.

for i in liste:
    try:
        if i not in sayilar:
            raise ZeroDivisionError #aslinda burda bir zeroDivison hatasi yok ama listedeki sayilari tespit etmeye calisiyoruz.
    except ZeroDivisionError as e: #zeroDivison yerine ValueError ya da baska bir hata ismi de verilebilirdi.
        continue
    else:
        print("2**%s = " %i, 2**i)
