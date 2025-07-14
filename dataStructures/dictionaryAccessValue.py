'''Challenge: 
 Write a function that takes a dictionary and a key as input and returns the value associated with that key. If the key is not present, return None.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_access = 'b'''''

#function to access the value of a key
def accessValue(key_to_access):
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    try:
        return my_dict[key_to_access]
    #return None if the key does not exist
    except KeyError:
        return None
    
key_to_access = input('Enter key: ')
print(accessValue(key_to_access))