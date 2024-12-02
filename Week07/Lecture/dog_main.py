from dog import Dog

d1 = Dog("Rosie", 2)
d2 = Dog("Buddy", 4)

print(d1.getName())
print(d2.getName())

print(d1.getBreed())
print(d2.getBreed())

d1.changeBreed("German Shephard")
print(d1.getBreed())
print(d2.getBreed())

d1.addFriend("Totoro")
d1.addFriend("Finn")

print(d1.getFriends())
print(d2.getFriends())

d1.addCloseFriend("Totoro")
d1.addCloseFriend("Finn")
print(d1.getCloseFriends())
print(d2.getCloseFriends())