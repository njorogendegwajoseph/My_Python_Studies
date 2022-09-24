x = [1,2,3,4,5,6]
y = [7,8]
x.append(y)
print(x)
#append can only add list in a list

z = [13,14,15,16]
x.extend(z)
print(x)
#extend also is applies to lists and doesnt carry the brackets. NB.

x.insert(0, "Jeremy")
print(x)
#Works well, hence prefarable is insert. First digit shows position, second is item.

del x[:2] #deletes the indices shown in the x list.
print(x)

x = [3, 5, 6, 9, 90]
del x[:2]
print(x)