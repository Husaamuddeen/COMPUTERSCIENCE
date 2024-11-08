'''Challenge: 
Develop a Python class for a Student.
The constructor should take parameters for the student's name, ID, and university major.
Implement private attributes for these parameters. 
Create methods to get and set the student's major, as well as to display the student's information. 

Instantiate more than one object from the class, and show suitable testing.  '''

#define student class
class Student:
    #private attributes name, id, major
    __name = ""
    __ID = ""
    __major = ""
    #constructor method
    def __init__(self, theName, theID, theMajor):
        self.__name = theName
        self.__ID = theID
        self.__major = theMajor
    #setters and getters
    def getMajor(self):
        return self.__major
    def setMajor(self, theMajor):
        self.__major = theMajor
    #method to display the info
    def printInfo(self):
        print(self.__name+", "+self.__ID+", "+self.__major)

#instantiate 2 students
student1 = Student("Husaam","1","computing")
student2 = Student("Eesa","10000000","cricket")
student1.printInfo()