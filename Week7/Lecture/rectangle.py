class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x_left = x1
        self.y_left = y1
        self.x_right = x2
        self.y_right = y2
        self.width = self.x_right - self.x_left
        self.height = self.y_left - self.y_right
    
    def __str__(self): # should return a string to be printed
        res = "*" * self.width + "\n"
        for i in range(self.height-2):
            row = "*" + " " * (self.width-2) + "*\n"
            res += row
        res += "*" * self.width + "\n"
        return res

    def calculateArea(self):
        return self.width * self.height
    
    def calculatePerimeter(self):
        return 2 * (self.width + self.height)


# main
r1 = Rectangle(10, 10, 25, 5)
print("Area:", r1.calculateArea())
print("Perimeter:", r1.calculatePerimeter())
print(r1)
        