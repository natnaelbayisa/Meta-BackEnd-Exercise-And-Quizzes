#reading with function its better for file handling and it closes the file 

file = open("ex14.file-handling.txt", mode="r")

data = file.readline()

print(data)

file.close()


#reading with function its better for file handling and it closes the file 
with open("ex14.file-handling.txt", "r") as file:
    print(file.read())

            # or
with open("ex14.file-handling.txt", "r") as file:
    data = file.readline()
    print(data)    
    