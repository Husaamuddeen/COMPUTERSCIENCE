'''Challenge: 
 Write a function that takes a dictionary and a key as input and returns True if the key is present in the dictionary, otherwise False.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'''

#function to check the precense of a key in the dictionary
def checkKey(dictionary1, key1):
    #loop through each key in the dictionary
    for key in dictionary1:
        if key == key1:
            return True
    return False

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(checkKey(my_dict, 'b'))