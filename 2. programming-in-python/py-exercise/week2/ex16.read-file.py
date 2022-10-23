       
"""
    read() - reads all lines / print all characters in the string
    file.read(40) - reads only the first 40 characters 
    readline() - read single line as a string
    file.readline(10) - reads only specified no of  characters on a line.
    readlines() - reads the entire content of the file and returns it an ordered list 
    
"""
    
with open("ex15.created-by-python.txt", "r") as file:
    #print(file.read()) # or use below code
    Lines = file.read()
    print(Lines)

                                            #The bestway is using the ff way

with open("ex15.created-by-python.txt", "r") as file:    
    for data in file:
        print(data)