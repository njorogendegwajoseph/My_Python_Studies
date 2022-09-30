x = "My name is Joseph Njoroge"
new_string = x.split(" ")
print(new_string)
a, b, *c = new_string
print(c)

cute = "I am a rockstar"
cutest = cute.split(" ", 1)
print(cutest)

#So, this is how we split.

test = "This is a test"
test2 = "-".join(test)
print(test2)