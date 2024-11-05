from person import Person

p1 = Person(name="John", myAge=25)
p2 = Person("Jack", 22)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p1)
print(p2)
"""
myList = []
myList.append(p1)
myList.append(p2)
print(myList)
"""

#p2.age = 35
p2.changeAge(35)
p2.changeName("DSA201")
print(p2)