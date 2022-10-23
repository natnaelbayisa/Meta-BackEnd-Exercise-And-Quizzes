set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

set_a.add(6)
print(set_a)

set_a.remove(6)
# set_a.discard(5)  # same as remove
print(set_a)

print(set_a.union(set_b))
# print(set_a | set_b) #same as union

print(set_a.intersection(set_b)) # show us values in both
# print(set_a & set_b) #same as intersection

print(set_a.difference(set_b)) #show us all values in set_a and not in set_b
# print(set_a - set_b) #same as difference

print(set_a.symmetric_difference(set_b)) #show us all thier d.ce values in set_a and in set_b
# print(set_a ^ set_b) #same as symmetric_difference

# set_a.update()
# print(set_a)

# for x in set_a:
#     print(x)