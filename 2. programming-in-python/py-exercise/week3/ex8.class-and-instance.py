class my_class:
    a = 5
    def sum(self,a,b): #without self keyword method doesn't work, use any key instead of self
        return a+b  #if no return value it says none after displaying the output
         
myClass = my_class()  #instance of class myClass is the object

print(my_class.a)   #attribute(class) reference

print(myClass.a)      #inherit from class -> attribute reference works with instance objects


print(myClass.sum(4,4))