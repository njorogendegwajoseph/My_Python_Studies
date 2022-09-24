#This section covers the sorted module

x = (23, 56, 78, 98, 94, 33) #tuple

y = sorted(x)
print(y) #Arranged from the least > highest

z = sorted(x, reverse = True)
print(z)
#using this reverse call rearranges from the max to the min.
#NB: tuples are not modifiable

print(3 in x)
print(3 not in x)
#These return booleans as the value.

new = [1,2,3]
new2 = [4,5,6]
new3 = new + new2
print(new3)
#Concatenate with the plus operator.

z = [None] * 20
print(z)
z[1] = "Mathhew"
print(z)
#This is for list initialization specitfying the space to be alocated.


numerical = [2, -2, 6, -5, 29]
print(min(numerical))
print(max(numerical))
#The min and the max modules find the largest and the smallest