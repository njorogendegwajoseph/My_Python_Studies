x = ["adam", 9, 23, "Levigne"]
print(x.index(9))
#The "index" keyword return the position of the word within the parenthesis.

y = x.count(9)
print(y)
#the count keyword  gives the number of times a word, value appears. You can reassign it to a variable.

#NESTING LISTS
original = [[0, 2], 4, 5]
copy = original[:]
copy[0] = 2
print(copy)
print(original)
#The [:] shallow copies and hence cannot access nested loops. Need to import copy
#variable.deepcopy(name)

