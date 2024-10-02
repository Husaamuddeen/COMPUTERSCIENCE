'''Challenge: 
Create a program that stores a list of 10 names.
Implement a linear search to check if a given name exists in the list.
Output whether the name was found or not.'''

#list of names
names = ['Husaam','Eesa','Kaya','Rezwan','Stevens','David','Sam','Eduard','Lessami','Maryam']

#linear search procedure
def linearSearch(names,search):
    #variable to indicate wether or not the input has been found
    found = False
    #keep track of how many index's the algorithm has checked
    count = 0
    #iterate through the list
    while not found and count < len(names):
        #check if the search is in the index of the list
        if search == names[count]:
            print('the name was found')
        #increment the index of the list
        count = count + 1
    if not found:
        print('the name was not found')

#user enters the name to seach for
search = input('Enter the name you are searching for: ')
linearSearch(search,names)