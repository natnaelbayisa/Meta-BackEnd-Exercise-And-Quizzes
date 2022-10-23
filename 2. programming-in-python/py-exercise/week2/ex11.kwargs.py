
def sum_of(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum += value
    return sum
# if want to round use this, return round(sum,2) 2 is amount of no u want round/ minimize decimal values.  
        
print(sum_of(tea=2.99, cake = 3.99, juice = 5.99))