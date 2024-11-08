'''Challenge: 
Create a Class for a dog in python. Implement private attributes using the _attribute approach in python.
When a dog is instantiated the constructor takes in two parameters, the name and colour.
These are the only attributes within the dog class.
 Also create a method that will take in a parameter integer and then output "Woof!" the number of times the value of the parameter. 
Create the necessary getter and setter methods for the object.
 Instantiate a new instance of a dog. output its name and colour in a single message e.g. Hello Fido, you are a Brown colour. 

Make the dog woof 10 times.
output the memory location of the Dog object you have instantiated.'''

#class for a dog
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
#instantiating a dog
myDog1 = Dog("Eesa eater","Red")
#print name and colour using the getters
print("Hello "+myDog1.getName()+", you are a "+myDog1.getColour()+" colour.")
#use the bark method to print woof 10 times
myDog1.bark(10)
