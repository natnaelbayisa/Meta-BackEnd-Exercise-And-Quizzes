#dictionary is key-value pair

my_dictionary = {1:"a", 2:"b",3:"c", 4:"c", 5:"e"}
my_d = {6:"n","o":"p",}

print(my_dictionary[1])

print(type(my_dictionary)) #type of my_dictionary

my_dictionary[4] = "d" #updating the 4th key
print(my_dictionary)

del my_dictionary[5] #delete my_dictionary at key 5
print(my_dictionary)

my_d[7] = "nati" #add a new value with key of 7
print(my_d)

my_d[6] = "not n Nati" #updating value at my_d at key 6
print(my_d)


my_dict = {1:"Test", "Name":"Nati"}

for key, value in my_dict.items(): # iterate on key and value
    print(str (key) + " : " + value)
    
# iterate only on keys

for x in my_dictionary:  
    print(x)