list1 = [1,2,3,4,5]
list2 = ["A", "B","C","D","E", list1[2]]
list3 = ["Z", True, 34, 9.00]
list4 = [6,[7,8,9],10,20]
list6 = [40,50,60,70]

print(list1[4]) 
print(list2)
print(list3)
print(list4[1][2])
print(*list1)
print(list1, sep =" ")

print(list1 + list2)
print(list1, list2)

#insert_to_list -> need to specify the index
list1.insert(len(list1), 90)
print(list1)

#append_to_list -> it doesn't need to specify the index
list1.append(80)
print(list1)

#extend_to_list -> it add one or more list to the list
list1.extend([100,200]) 
print(list1)

#remove_list
list1.pop(0)
print(list1)

del list1[0]
print(list1)

#for_loop

for x in list1:
    print("value", x)

