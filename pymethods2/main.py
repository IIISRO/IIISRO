class Vehicle:

    _numofWheels = 4
    _color = "black"
    engine = "thermal"
    positionX = 0
    positionY = 0
    speed = 160
    isOn = False

    def accelerate(self):
        self.speed =self.speed+ 1
        return self.speed

    def moveForward(self, positionX, positionY):
        positionX += 30
        positionY += 40
        return positionX, positionY

    def moveBackwards(self, positionX, positionY):
        positionX -= 30
        positionY -= 20
        return positionX, positionY

    def ignition(self):
        if self.isOn == True: 
            self.isOn == False
        else: 
            self.isOn = True

    @property
    def numOfWheels(self):
        return self._numofWheels
       
    @numOfWheels.setter
    def numOfWheels(self, num):
        self._numofWheels = num

    @property
    def color(self):
        return self._color
       
    @color.setter
    def color(self, name):
        self._color = name

class Motorcycle(Vehicle):
 
    brand = "Yamaha"
    numofSeats = 4
 
    def __init__(self, color, engine, wheels):
        super().__init__()
 
    def getBrand(self):
        return self.brand
    
    def getnumofSeats(self):
        return self.numofSeats
    
    def setBrand(self, brand):
        return brand
    
    def setnumOfSeats(self, numofSeats):
        return numofSeats
    
    def accelerate(self):
        self.speed += 10
        return self.speed
    
    def decelerate(self):
        self.speed -= 10
        return self.speed

vehicle = Vehicle()
motorcycle = Motorcycle('black', 'thermal', 2)

print(vehicle.accelerate())
print(vehicle.moveForward(50, 60))
print(vehicle.moveBackwards(50, 60))
print(vehicle.numOfWheels)

vehicle.numOfWheels = 2

print(vehicle.numOfWheels)
print(vehicle.color)

vehicle.color = "black"

print(vehicle.color)
print(motorcycle.getBrand())
print(motorcycle.getnumofSeats())
print(motorcycle.setBrand("lada"))
print(motorcycle.setnumOfSeats(2))
print(motorcycle.accelerate())
print(motorcycle.decelerate())