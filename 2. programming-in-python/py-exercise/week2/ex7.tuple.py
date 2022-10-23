# tuples accept any type of data types like string, double, boolean, integer.

my_tuple = (1,2,3,"dell",True, 4.5) # using bracket is advanced

print(my_tuple[5]) #tell us the value in index 5
print(type(my_tuple)) #tell us type of the variable
print(my_tuple.index("dell")) #tell us the index of the value
print(my_tuple.count(1)) #tell us how many its repeated

# iterate on my_tuple
for x in my_tuple:
    print(x)
    
