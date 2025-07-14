'''Challenge: 
 Write a function that takes a dictionary, a key, and a new value as input and updates the value associated with that key in the dictionary. 

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_update = 'b'
new_value = 5'''

#function to update the value of a key in a dictionary
def updateValue(dict,key,value):
    dict[key] = value
    return dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_update = 'b'
new_value = 5

my_dict = updateValue(my_dict,key_to_update,new_value)

print(my_dict)