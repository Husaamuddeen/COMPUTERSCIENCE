#function to implement quicksort on a list
def quickSort(unsorted):
    #choose the pivot to be the first item in the unsorted list
    pivot = unsorted[0]
    left = []
    right = []
    for i in range(0,len(unsorted)):
        if unsorted[i] < pivot:
            #make a left list for all the items smaller than the pivot
            left.append(unsorted[i])
        elif unsorted[i] > pivot:
            #make a right list for all the items bigger than the pivot
            right.append(unsorted[i])
    #if a list is length 1 or 0, it is sorted and can be returned to the previous recursion
    if len(left) > 1:
        left = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)
    #after the call stack has unravelled, construct the list with the left and right lists and the pivot
    newUnsorted = left
    newUnsorted.append(pivot)
    newUnsorted = newUnsorted + right
    return newUnsorted

unsortedList = [45,23,76,47,19,38,2345,76,132,765,3657,76,3457,3,67,34,90,79]
sorted = quickSort(unsortedList)
print(sorted)