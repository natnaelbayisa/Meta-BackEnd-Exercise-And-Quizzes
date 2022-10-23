def sum(n):
    if n == 1:
       return 0
    return n + sum(n-1)

a = sum(5)
print(a)


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)


a = [[96], [69]]

print(''.join(list(map(str, a))))


z = ["alpha","bravo","charlie"]
new_z = [i[0]*2for i in z]
print(new_z)

#accept input
print("Where do you live?")
location = input()
print("So you live in " + location)

#passing value
def say_hello(you):
    return "Hello " +  you
print(say_hello("Nati"))

# two ways of concatinating
str1 = input("first name: ")
str2 = input("second name: ")

print("hello {} {}" .format(str1, str2)) 
print("hello" + ' ' + str1 +' ' + str2)

#bla bla blaaaaaaaaaaaaaa
print("N"); print("g")