
try:
    f = open("deneme.txt", "r")
except IOError:
    print("Dosya acilamiyor")
finally: #hata alinsa da alinmasa da bu blok calisicak.
    if f:
        f.close()