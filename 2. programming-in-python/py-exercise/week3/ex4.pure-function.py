my_list = [1,2,3]

#pure function doesn't update or create
def add_list(lst,item):
    n1 = lst.copy()
    n1.append(item)
    return n1

       
new_list = add_list(my_list, 4)

print(my_list)
print(new_list)
print("------------------------------------------>")

#the ff isn't pure function
def add_new_list(lst,item):
    lst.append(item)
    return lst

new_data = add_new_list(my_list, 4)

print(my_list)
print(new_data)
