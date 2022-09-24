x = ["Name", "Luca", "John", "Amos"]
y = [4, 7, 9, 9]

x[0:3] = y[0:3]
print(x)
#This is replacement of items in a list from anothe list or random.

x[0:3] = "Calysy", "Mayor", "Mandatory"
print(x)

x[len(x):] = [2, 4, 9, 80]
print(x)
#This one appends to the end of the list. Now, use the len function to show end of the list.

x[:0] = [9, "John"]
print(x)
#This one appends at the front.

x[:0] = []
print(x)
#deletes everything from list.