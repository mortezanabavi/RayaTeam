class Car:

    def __init__(self, name, color):
        self.speed = 0
        self.name = name
        self.color = color

    def setSpeed(self, speed):
        self.speed = speed
        
    def setColor(self, color):
        self.color = color


carClass = Car("Neysan", "blue")
print(carClass.name)
print(carClass.speed)
print(carClass.setSpeed(10))
print(carClass.speed)
print(carClass.color)
print(carClass.setColor("red"))
print(carClass.color)