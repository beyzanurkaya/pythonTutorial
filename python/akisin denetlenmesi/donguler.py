import math

list1 = [99, 98, 97]
list2 = [1, 3, 7, 11, "cicek", "bocek", list1]

for n in list2:
    print(n)

i = 0
while i < 5:
    print(i)
    i+=1

print("------------")

j = 0
while True:
    print(j)
    j+=1
    if j>5:
        break

print("------------")

a = 0
while True:
    a+=1
    if a % 2 == 0:
        continue
    elif a > 10:
        break
    else:
        print(a)

l1 = []
l2 = []
l3 = []

for n in range(17): #range(son)
    l1.append(n)
print("l1 = ", l1)


for n in range(2, 11): #range(ilk, son)
    l2.append(n)
print("l2 = ", l2)


for n in range(5, 24, 3): #range(ilk, son, adim)
    l3.append(n)
print("l3 = ", l3)



