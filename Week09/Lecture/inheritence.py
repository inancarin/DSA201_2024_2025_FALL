# it will be a parent / super class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "A person whose name is " + self.name + ", and age is " + str(self.age)
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def changeAge(self, newAge):
        self.age = newAge
    
    def changeName(self, newName):
        self.name = newName


# this class will be a sub/child class of Person class
class Student(Person):
    def __init__(self, name, age, id, school):
        #self.name = name
        #self.age = age
        super().__init__(name, age)
        self.id = id
        self.school = school
    
    def __str__(self):
        return "A student with ID: " + str(self.id) + " in " + self.school

    def getID(self):
        return self.id
    
    def getSchool(self):
        return self.school

class Doctor(Person):
    def __init__(self, name, age, hospital):
        #self.name = name
        #self.age = age
        super().__init__(name, age)
        self.hospital = hospital
    
    def __str__(self):
        return "Dr. " + self.name + " at " + self.hospital

# main part
p1  = Person("John", 25)
print(p1)
p1.changeAge(24)
print(p1)

s1 = Student("Ahmet", 20, 1, "Sabanci University")
print(s1)
print(s1.getName())
print(s1.getSchool())

d1 = Doctor("Ayse", 45, "Acibadem Hospital")
print(d1)
print(d1.getAge())