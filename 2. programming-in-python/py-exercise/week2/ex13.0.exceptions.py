def divide_by(a,b):
    return a/b

#its like try catch in js

try:
    ans = divide_by(10,0)
    print(ans)
except Exception as e:       #base class Exception is used for all exceptions that are written within Python.
    print("Sth went wrong", e) 
    print(e.__class__) #tell us the error class
    
try:
    ans = divide_by(20,0)
    print(ans)
except ZeroDivisionError as e: # e is a variable acts as alias for the exception
    print(e, "We cannot divide by zero")  #print user friendly error
    print(e. __class__)
except Exception as e:
    print("Sth went wrong")
    