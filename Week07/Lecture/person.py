class Person:
    
    def __init__(self, name, myAge):
        self.name = name
        self.age = myAge

    def __str__(self):
        return "A person whose name is " + self.name + " and age is " + str(self.age)
    
    def __repr__(self):
        return self.name + " - " + str(self.age)

    # getter methods
    def getAge(self):
        return self.age

    # setter method
    def changeAge(self, newAge):
        if isinstance(newAge, int) and newAge > 0:
            self.age = newAge
        else:
            print("Invalid age value, so I do not change the age")
    
    # getter
    def getName(self):
        return self.name

    # setter methods
    def changeName(self, newName):
        if isinstance(newName, str) and newName.isalpha():
            self.name = newName
        else:
            print("Invalid new name, so do not change it")