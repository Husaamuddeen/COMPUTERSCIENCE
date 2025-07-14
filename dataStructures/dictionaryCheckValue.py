'''Challenge: 
 Write a function that takes a dictionary and a value as input and returns True if the value is present in the dictionary, otherwise False.

my_dict = {'a': 1, 'b': 2, 'c': 3}
value_to_check = 2'''

#function to check the precense of a value in a dictionary
def checkPrecense(dictionary1,value1):
    #loop through each value in the dictionary
    for key in dictionary1:
        if dictionary1[key] == value1:
            return True
    return False

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(checkPrecense(my_dict,2))