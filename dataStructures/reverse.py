'''Challenge: 
 Write a function that takes a list as input and returns a new list with the elements reversed.'''

list1 = [543534,5645,64564345,6456,45645,645,34,5456,45]

#function to reverse a list
def reverse(list1):
    length1 = len(list1)
    for i in range(0,length1//2):
        #temporary variable to store the value of the element being overrwitten
        temporary = list1[i]
        list1[i] = list1[length1-1-i]
        list1[length1-1-i] = temporary
    return list1

print(reverse(list1))