'''Challenge: 
 Write a function that takes a dictionary, a key, and a value as input and adds the key-value pair to the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
new_key = 'd'
new_value = 4'''

#function to add a pair to a dictionary
def addPair(dict,key,value):
    dict[key] = value
    return dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
new_key = 'd'
new_value = 4

my_dict = addPair(my_dict,new_key,new_value)
print(my_dict)