
list1 = [] #bos liste
list2 = [1,2,3]
list2[1] = 21 #listenin elemanlari degistirilebilir
list3 = [1, "string", list2, ('abc', 'xxx', '5')] #indileri sifirdan baslar

print(list1)
#print(list)
print(list2)
print(list3)

#liste dilimleme (sliceable)

*hepsi, son = ["ilk", 1, 2.5, 3, 9]
print(hepsi)
print(son)

ilk, *orta, son= [7, 11, 63, 5, 742, "bezbebek"]
print(ilk)
print(orta)
print(son)





