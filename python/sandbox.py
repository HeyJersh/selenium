"""
Learning Python
Author: Joshua Gomez
"""

# Variables and Objects
a = 10
b = 20
c = 30

learning = True
expert = False

string = "Some bit of \"string\" and stuff"
string2 = "abc123abc123ggglllaaa"

my_work = "my work"
code = "code"

# Math and Methods
print (a * b)
print (a / c)
print (a % c)
print (c ** a)
print (learning)
print (expert)

#lowercase everything
print (string.lower())

#Uppercase everything
print (string.upper())

#length of a string
print (len(string))

#string concat
print (string + str(2))
print (string + ". " + "Boop.")

# Replace stuff
print (string2.replace("abc", "BEEP", 1))

# Grab characters [array starting index:index end:step]
print (string2[0:12:3])
print (string[:-1])
print (string[::-1])
# Format strings
print ("Welcome to %s and enjoy the %s." % (my_work, code))

# Lists
list = ["thing", "another", "poop"]
print (list)
list.append("stuff")
list.insert(1, "junk")
print (list)
print (list.sort())
print (list.index("stuff"))
print (list.pop())
print (list)
list.remove("poop")
print(list)
slicing = list[0:2]
print (slicing)

# Conditional Logic
if a < b:
    print ("a is NOT bigger")

if a > b:
    print ("a is WAY bigger")
elif a == a:
    print ("a is " + str(a))
else:
    print ("a is still not bigger...")

x = 1
while x < 10:
    print ("Do something dumb")
    x+=1

for n in list:
    print (n)

for num in range(1, 101, 2):
    print (num)

# More Methods
def test_method(num1, num2):
    print(num1 + num2)

test_method(1, 1)

# Classes and Objects
class Person(object):
    def __init__(self, name):
        self.name = name
    def sit(self):
        print("Sat down.")

josh = Person("Josh")
josh.sit()