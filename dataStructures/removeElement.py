'''Challenge: 
 Write a function that takes a list and an element as input and removes the first occurrence of the element from the list.'''

#function to remove an element from a list at first occurence
def removeElement(list1,element):
    #conditions for the loop
    found = False
    counter = 0
    #loop through the list
    while not found and counter <= len(list1):
        if list1[counter] == element:
            found = True
            #remove element from index
            list1[counter] = ''
