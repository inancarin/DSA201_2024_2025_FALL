class Vehicle:
  def __init__(self, color, tireNumber):
    self.color = color
    self.tireNumber = tireNumber

  # getter
  def getColor(self):
    return self.color

  def getTireNumber(self):
    return self.tireNumber

  def changeColor(self, newColor):
    self.color = newColor

  def changeTireNumber(self, newNumber):
    self.tireNumber = newNumber