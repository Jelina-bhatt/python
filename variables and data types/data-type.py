#You can get the data type of any object by using the type() function
x="hello world"
#print x
print(x)
#print data type of x
print(type(x))
x=3
#print x
print(x)
#print data type of x
print(type(x))

x=4.6
print(x)
print(type(x))

#for list
x=1j
print(x)
print(type(x))

#list,tuple and range are used for sequence type

#for list
x=['apple',"banana","orange"]
print(x)
print(type(x))

#for tuple
x=("apple","banana","orange")
print(x)
print(type(x))

#for range
x=range(6)
print(x)
print(type(x))

#for dict
#dict is used for mapping type
x={"name":"jelina", "age":"20"}
print(x)
print(type(x))

#for set
x={"apple","banana","orange"}
print(x)
print(type(x))

#for frozenset
x=frozenset({"apple","banana","orange"})
print(x)
print(type(x))
#set and frozenset are set data type

#for boolean set
x=True
print(x)
print(type(x))

#for binary types:bytes, bytesarray, memoryview
#for bytes
x="hello-jelina"
print(x)
print(type(x))

#bytesarray
x=bytearray(5)
print(x)
print(type(x))

#for memoryview
x=memoryview(bytes(5))
print(x)
print(type(x))

#for none
x=None
print(x)
print(type(x))

#for type conversion
j="03.01"
d=float(j)
k=type(d)
print(k)
