#parametrelerin tip, sinif veya deger kontrolu
#veri yapilarindaki degismezlerin denetimi
#bir fonksiyon cagrisindan donen degerlerin denetimi
#asla olmaz denilern kosullarin denetimi

def assert_kontrol(n):
    assert type(n)== int , "parametre tipi int olmali" #bu satir konmasa bile hata alinacaktı ama nedenini arastirmak zorunda kalacaktik.
    return n**2

print(assert_kontrol(15))
print(assert_kontrol('s'))
print(assert_kontrol(-7))