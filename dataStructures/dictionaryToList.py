'''Dictionary: Values List
⭐⭐⭐⭐

Challenge: 
 Write a function that takes a dictionary as input and returns a list containing all the values in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}'''

my_dict = {'a': 1, 'b': 2, 'c': 3}

#function to make a list of values in a dictionary
def dictToList(dict1):
    list1 = []
    #loop through each key in the dictionary
    for key in dict1:
        list1.append(key)
    return list1

list1 = dictToList(my_dict)
print(list1)