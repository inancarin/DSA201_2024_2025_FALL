class Dog:
    
    breed = "Poodle" # class variable/attribute
    friends = []     # class variable/attribute

    def __init__(self, name, age):
        self.name = name        # instance variable/attribute
        self.age = age          # instance variable/attribute
        self.closeFriends = []  # instance variable/attribute

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getBreed(self):
        return self.breed
    
    def changeBreed(self, newBreed):
        self.breed = newBreed
    
    def addFriend(self, newFriend):
        self.friends.append(newFriend)
    
    def getFriends(self):
        return self.friends
    
    def getCloseFriends(self):
        return self.closeFriends
    
    def addCloseFriend(self, newFriend):
        self.closeFriends.append(newFriend)