x = set([1,2,3,4,5])
y = set([3,4,5,6,7,8])
print(x&y)
print(x|y)
print(x^y)
# | is for unions, prints all the values, but deletes repeated.
# & is for intersection, prints the values that overlap.
# ^ is for symmetric difference, basically opposite of &.

#Forzen sets
z = set([1,2,3,4])
new = frozenset(x)

z.add(new)
print(z)
#A fozenset can be added to a set.

t = set([1, 2, 5, 1, 0, 2, 3, 1, 1, (1,
2, 3)])
print(count(t))