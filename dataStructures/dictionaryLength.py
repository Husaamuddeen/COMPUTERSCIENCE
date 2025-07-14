'''
Challenge: 
 Write a function that takes a dictionary as input and returns the number of key-value pairs in the dictionary. 

my_dict = {'a': 1, 'b': 2, 'c': 3}'''

my_dict = {'a': 1, 'b': 2, 'c': 3}
count = 0
for key in my_dict:
    count = count + 1
print(count)