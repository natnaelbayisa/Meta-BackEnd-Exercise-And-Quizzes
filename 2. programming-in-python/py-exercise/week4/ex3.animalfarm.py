def d():
    animal = "elephant"
    
    def e():
        nonlocal animal #nonlocal is special scope nested function 
        animal = "giraffe"
        print("Inside nested functions: " + animal) #2nd output
        
    print("Before calling function: " + animal) #1st output
    e()
    print("After nested functions: " + animal) #3rd output
    
animal = "camel"
d()
print("Global animal: " + animal) #4th output as a global value
