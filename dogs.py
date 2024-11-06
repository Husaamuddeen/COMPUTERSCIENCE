class Dog:
    #private name
    __name = ""
    #private colour
    __colour = ""
    #public constructor
    def __init__(self, theName, theColour):
        self.__name = theName
        self.__colour = theColour
    #public bark method
    def bark(self, barkTimes):
        for i in range(0,barkTimes):
            print("Woof!")
    #public colour setter
    def setColour(self, newColour):
        self.__colour = newColour
    #public colour getter
    def getColour(self):
        return self.__colour
    #public name getter
    def getName(self):
        return self.__name
myDog1 = Dog("Eesa eater","Red")
myDog2 = myDog1
print(myDog1)
print(myDog2)
newColour = input("enter the new colour of the dog: ")
myDog1.setColour(newColour)
print(myDog1.getColour())
print(myDog2.getColour())

class Cat:
    __name = ""
    __health = ""
    __attack = ""
    def __init__(self, theName, theHealth, theAttack):
        self.__name = theName
        self.__health = theHealth
        