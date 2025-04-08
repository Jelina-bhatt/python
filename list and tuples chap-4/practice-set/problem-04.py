# wap to check tuple type cannot be changed in python

a=(2,3,"jelina",7)
a[2]="bhatt" #'tuple' object does not support item assignment even if it a string or same data type
a[3]=0
print(a)