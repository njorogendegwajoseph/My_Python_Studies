##Searching;
 #   """The 're' module comprehensively used in searching.
 #       This module looks for a pattern.
 #           The four basic string-searching methods are similar: find, rfind, index, and
 #               rindex.
 #           A related method, count, counts how many times a substring can be found
 #            in another string.
 #            1.find takes one required argument: the substring being searched for
 #            2.find returns
 #           the position of the first character of the first instance of substring in the string
 #           object, or –1 if substring doesn’t occur in the string:
 #   """
stringy = "My name is Arnold Swazzneger"
print(stringy.rfind("name")) #position

stringy = "My name is Arnold Swazzneger"
print(stringy.count("a")) #no of times.

stringy = "My name is Arnold Swazzneger"
print(stringy.rfind("ZZAs")) #does not appear -1.

#find can also take one or two additional, optional arguments. The first of these arguments,
#if present, is an integer start; it causes find to ignore all characters before
#position start in string when searching for substring. The second optional argument,
#if present, is an integer end; it causes find to ignore characters at or after position
#end in string: