#Sorting modules using  functions.Modules.

def compare_no_of_char(_string):
    return len(_string)

string1 = ["Name", "Lucas", "is"]
print(string1)
string1.sort()
print(string1)
#this is the normal sort module>

string1.sort(key=compare_no_of_char)
print(string1)
#Custom sort uses the "key" word before the function name inside the parenthesis to guide it on how to sort.
#In the above example, I used the length of the string to sort.

string1.sort(key=two_letter_string)
print(string1)