numbers = [1,2,4,5,7,9,12,18,38,53,56,89,101,129,175]
def binarySearch(numbers, search):
    startPointer = 0
    endPointer = len(numbers)-1
    found = False
    complete = False
    print(startPointer)
    print(endPointer)
    while not complete:
        print('start')
        print(startPointer)
        print(endPointer)
        midPoint = startPointer+(endPointer-startPointer)//2
        print(midPoint)
        if numbers[midPoint] < search:
            startPointer = midPoint + 1
        elif numbers[midPoint] > search:
            endPointer = midPoint -1
        elif numbers[midPoint] == search:
            complete = True
            found = True
            position = midPoint
            print('the search query was found in position '+str(position+1)+' of the list')
        if startPointer == endPointer and startPointer == midPoint:
            complete = True
        print('MIDDLE')
        print(startPointer)
        print(endPointer)
        print(midPoint)
    if not found:
        print('the search query was not found')
search = int(input('enter the number to search for: '))
binarySearch(numbers, search)