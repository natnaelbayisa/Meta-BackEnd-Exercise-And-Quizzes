# Starter code -> add except handling for all examples
##########################################################
# Starter code
# items = [1,2,3,4,5]
# item = items[6]
# print(item)

#solution
items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)

except:
    print("Item doesn't exist in the list")

##############################################################

##############################################################
"""
In math there are rules about dividing by zero. The below code is trying to do just
that and will throw a ZeroDivisionError. 
Add exception handling to return back 0 instead of allowing the error to be thrown.
"""
# Starter code
# def divide_by(a, b):
#     return a / b


# ans = divide_by(40, 0)
# print(ans)


# Solution
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print("Sth went wrong",e)
        
ans = divide_by(40, 0)
print(ans)
##############################################################

"""
FileNotFoundError
The code below is looking for a file that does not exist.
Add exception handling to catch this error and return the following "The file could not be found".
"""
# Starter code
# with open('file_does_not_exist.txt', 'r') as file:
#     print(file.read())

# solution
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
    
except:
    print("The file could not be found")

##############################################################################