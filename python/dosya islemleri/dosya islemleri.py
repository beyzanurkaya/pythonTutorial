#izinler
"""""
“r”	Dosyayı okuma yetkisi verir. Eğer okunacak dosya dizinde mevcut değilse hata mesajı döndürür.
“w”	Dosyaya yazma yetkisi verir. Eğer dizinde aynı isimde bir dosya varsa onu siler ve yeni boş bir dosya oluşturur.
“a”	Dosyaya yazma yetkisi verir. Eğer dizinde aynı isimde bir dosya varsa onu silmez, sonuna ekleme yaparak yazar.
“x”	Dosyaya yazma yetkisi verir. Eğer dizinde aynı isimde bir dosya varsa hata mesajı döndürür.
“r+”	Hem okuma hem de yazma yetkisi verir. Dosya önceden mevcut olmalıdır.
“w+”	Hem okuma hem de yazma yetkisi verir. Dosya o dizinde mevcut değilse siler ve aynı isimde yenisini oluşturur.
“a+”	Hem okuma hem de yazma yetkisi verir. Dosya o dizinde mevcutsa hata mesajı döndürür.
“rb”	İkili (binary) dosyalar için okuma yetkisi verir. Dosya o dizinde mevcut olmalıdır.
“wb”	İkili (binary) dosyalar için yazma yetkisi verir. Eğer dosya o dizinde varsa siler ve aynı isimde yenisini oluşturur.
“ab”	İkili (binary) dosyalar için yazma yetkisi verir. Eğer dosya o dizinde varsa sonuna ekleme yapılır.
“xb”	İkili (binary) dosyalar için yazma yetkisi verir. Eğer dosya o dizinde varsa hata mesajı üretir.
“rb+”	İkili (binary) dosyalar için hem okuma hem de yazma yetkisi verir. Dosya o dizinde mevcut olmalıdır.
“wb+”	İkili (binary) dosyalar için hem yazma hem de okuma yetkisi verir. Eğer dosya o dizinde varsa siler ve aynı isimde yenisini oluşturur.
“ab+”	İkili (binary) dosyalar için hem yazma hem de okuma yetkisi verir. Eğer dosya o dizinde varsa sonuna ekleme yapılır.
“xb+”	İkili (binary) dosyalar için hem yazma hem de okuma yetkisi verir. Eğer dosya o dizinde varsa hata mesajı üretir.
"""""

f = open("dosya.txt")
#print(f.read())
#print(f.readline()) #satir satir okur
#print(f.read(10)) #10 karakter oku

for l in f:
    print(l)

f.close()

fileToAppend = open("deneme.txt", "a") #varolan datanin yanina yazar
#w varolan datanin ustune yazar
fileToAppend.write("Beyza Nur Kaya")
fileToAppend.write("\n")
fileToAppend.write("Ece Deniz Koksal")
fileToAppend.close()

import os

if os.path.exists("deneme.txt"): #dosya varsa dosyayi sil
    #os.remove("deneme.txt")
else:
    print("Boyle bir dosya yok.")
#os.remove("dosya.txt") #dosyayi sil

#os.rmdir("empty") klasor silme