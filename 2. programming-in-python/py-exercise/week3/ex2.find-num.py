
#linear
def find_num(num):
    count = 0

    for i in range(100):
        if i == num:
            print("Total iteration:" + str(count))
            return i
        count += 1 
    
find_num(89)

#binary ------------------->doesn't work fix later
def find_num_log(target):
    iteration = 0
    x = range(100)
    left = 0
    right = len(x) - 1
    
    while left <= right:
        iteration += 1
        middle = (right+left)
        isNumber = x[middle]
    
    if target == isNumber:
        print("Iteration", iteration)
        return middle
    elif target < isNumber:
        right = middle - 1
    else:
        left = middle + 1
    return -1
print(find_num_log(97)) 


#Quadratic

for x in range(10):
    for y in range(10):
        print(x,y)