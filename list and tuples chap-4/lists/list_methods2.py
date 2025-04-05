#combining lists
l1=[1,2]
l2=[3,4]
combined= l1 + l2
print(combined)

#copying a list
newlist=l1.copy()
print(newlist)
l1[1]=80
print(l1)
print(1 in l1)