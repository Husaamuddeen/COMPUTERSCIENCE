'''Challenge: 
 Write a function that takes two dictionaries as input and returns a new dictionary containing key-value pairs from both dictionaries.
   If a key is present in both dictionaries, use the value from the second dictionary.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}'''

#function to merge dictionaries
def mergeDictionaries(dictionary1, dictionary2):
    newDictionary = {}
    #loop through dictionary 1 and add each key value pair
    for key in dictionary1:
        newDictionary[key] = dictionary1[key]
    #loop through dictionary 2 and add each key value pair
    for key in dictionary2:
        newDictionary[key] = dictionary2[key]
    return newDictionary

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

newDict = mergeDictionaries(dict1,dict2)
print(newDict)