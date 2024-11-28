'''Design a Python class for a Vehicle. Implement attributes for make, model, and year.
 Then, create subclasses for different types of vehicles such as Car, Truck, and Motorcycle.
 Each subclass should have additional attributes or methods specific to its type.'''

#defining vehicle superclass
class Vehicle:
    #private make, mode, year
    __make = ""
    __model = ""
    __year = ""
    #constructor
    def __init__(self, theMake, theModel, theYear):
        self.__make = theMake
        self.__model = theModel
        self.__year = theYear
    
#defining car subclass
class Car(Vehicle):
    #private speed
    __speed = ""
    #private constructor
    def __init__(self, theMake, theModel, theYear, theSpeed):
        super().__init__(theMake, theModel, theYear)
        self.__speed = theSpeed

#defining truck subclass
class Truck(Vehicle):
    #private seats
    __seats = ""
    def __init__(self, theMake, theModel, theYear, theSeats):
        super().__init__(theMake, theModel, theYear)
        self.__seats = theSeats

#defining motorcycle subclass
class Motorcylce(Vehicle):
    #private cc
    __cc = ""
    def __init__(self, theMake, theModel, theYear, theCc):
        super().__init__(theMake, theModel, theYear, theCc)
        self.__cc = theCc

#instantiating a car
make = "ferrari"
model = "laferrari"
year = "2024"
speed = "200"
myCar = Car(make,model,year,speed)
        