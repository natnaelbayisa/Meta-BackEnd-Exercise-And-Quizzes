country = "Ethioia"

print("Country Name: " + country)

print(globals()) #cause of this function the above statement isn't printed
print("-------------------------->")

def b():
    country = "Germany"
    print("Country Name: " + country)
    
    print(locals()) #this function represents the local variable and prints local value

b()

print("Country Name: " + country)
