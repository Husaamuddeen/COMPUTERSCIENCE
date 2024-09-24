#variable to show wether or not the file has been read correctly
complete = False
while not complete:
    try:
        #try to open file
        filename = input('enter the name of your file: ')
        myFile = open(filename,'r')
        myline = myFile.readline()
        #read each line until none
        while myline:
            print(myline)
            myline = myFile.readline()
        myFile.close() 
        complete = True
    #except if the file doesnt exist
    except FileNotFoundError:
        print('This file does not exist')
    #except if the file is not a text
    except UnicodeDecodeError:
        print('This file is not a text file')