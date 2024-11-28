'''Challenge: 
Write a program that takes a users name, opens a text file, and writes the name to the end of the file'''

#open the text file
numbers = open("numbers.txt","w")
#write a number in each iteration of the for loop
for i in range(0,10):
    numbers.write("\n")
    numbers.write(str(i))

#close the file
numbers.close()