'''Challenge: 
 Write a function that takes two lists as input and returns a new list containing elements from both lists'''

#function to concatenate lists
def concatenate(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    newList = []
    #copy each element in list 1 to the new list
    for i in range (0,length1):
        newList.append(list1[i])
    #copy each element in list 2 to the new list
    for i in range (0,length2):
        newList.append(list2[i])
    return newList

list1 = [4,767,3,45,67,78,45,6,567,56]
list2 = [55,3,54667,235765,735,5756,7]

newList = concatenate(list1,list2)
print(newList)