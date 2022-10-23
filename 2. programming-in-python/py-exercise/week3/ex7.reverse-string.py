list = ["A", "B", "C", "D"]

#reverse string
list.reverse()
print(list)

print("------------------------------------>")

#reverse list by forloop
for lists in list:
    lists[::-1]
    print(lists)
    
print("------------------------------------>")

#normal string reversal    
reverse = "reversal"
new_list = reverse[::-1]
print(new_list)

print("------------------------------------>")


"""
the else statement can do this
I add a slice function by typing the open square bracket,
the number one, and a colon followed by the closed square bracket.
This time the string is traversed from the front, skipping the first 
character in every loop and this first character skipped is appended to the remaining string. 
"""
#by using function to reverse string
def rev_string(str):
    if len(str) == 0:
        return str
    else:
        return rev_string(str[1:]) + str[0]
    
str = "dell"
reverse = rev_string(str)
print(reverse)


