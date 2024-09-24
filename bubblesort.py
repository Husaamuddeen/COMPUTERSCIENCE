unsortedList = [645,56,87,234,76]
#cycle through each bubble
# 56,4,13,56,7,5,34,5,56,7,1,34,8967,45,56,29
def bubbleSort(unsortedlist):
    #temporary variable to store the value of the element being written over
    temporary = 0
    swap = 1
    #when no swaps happen in an iteration, the list is sorted, so the loop ends when there are no swaps
    while swap != 0:
        swap = 0
        #iterate through the loop, swapping an element with the element in front of it if it is larger
        for i in range(len(unsortedList)-1):
            if unsortedList[i]>unsortedList[i+1]:
                temporary = unsortedList[i]
                unsortedList[i] = unsortedList[i+1]
                unsortedList[i+1] = temporary
                swap = swap + 1
    return unsortedList

def insertionSort(unsortedList):
    temporary = 0
    for i in range(1,len(unsortedList)):
        swap = 1
        for j in range(0,i):
            temporary = 0
            if unsortedList[i-j] < unsortedList[i-j-1]:
                temporary = unsortedList[i-j]
                unsortedList[i-j] = unsortedList[i-j-1]
                unsortedList[i-j-1] = temporary
                swap = swap + 1
    return unsortedList

print(insertionSort(unsortedList))
