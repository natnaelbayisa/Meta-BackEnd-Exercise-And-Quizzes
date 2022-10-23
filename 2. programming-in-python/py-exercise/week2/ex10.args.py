# def sum_of(a,b):
#     return a+b

# print(sum(2,3,4))

#The above example have an error to fix it we can use args an kwargs(key word args)  

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
        
print(sum_of(4,5,6))