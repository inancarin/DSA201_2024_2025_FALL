from vehicle import Vehicle

v1 = Vehicle("red", 4)
v2 = Vehicle("blue", 2)

print(v1.getColor())
print(v2.getColor())

v2.changeColor("Black")
print(v2.getColor())