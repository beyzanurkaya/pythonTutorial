
for n in range(5):
    try:
        m = 5/(3-n)
    except ZeroDivisionError as e:
        print("5/(3-3) = Tanimsiz")
    else:
        print("5/(3-%s) = " % n,m)

print("---" * 10)

for n in range(5):
    try:
        m = 5 / (3 - n)
        print("5/(3-%s) = " % n, m)
    except ZeroDivisionError as e:
        print("5/(3-3) = Tanimsiz")

#else cok kullanilan bir yontem degildir.