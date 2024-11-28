'''Challenge: 
Define a Python class for a Rectangle.
The constructor should take parameters for the length and width of the rectangle.
Implement private attributes for these parameters.
Create methods to calculate the area and perimeter of the rectangle.

Instantiate more than one object from the class, and show suitable testing.  '''

#define rectangle class
class Rectangle:
    #private length and width
    __length = 0
    __width = 0
    #constructor method
    def __init__(self, theLength, theWidth):
        self.__length = theLength
        self.__width = theWidth
    #method to calculate the area
    def calcArea(self):
        return self.__length*self.__width
    #method to calculate the perimeter
    def calcPerimeter(self):
        return (self.__length*2+self.__width*2)

#instantiate an object
rectangle1 = Rectangle(5,2)
print(rectangle1.calcArea())
print(rectangle1.calcPerimeter())