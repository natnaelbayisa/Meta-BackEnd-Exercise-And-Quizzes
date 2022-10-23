alphabets = ["a","b","c","d","----------->"]

#for loop
for item in alphabets:
    print("alphabets are", item)
    
#another option of for loop -> counting index
for idx, item in enumerate(alphabets):
    print(idx,item)   
    
# while loop
item = 0

while item < len(alphabets):
    print("alphabets are", alphabets[item])
    item +=1

#----------------------------------------->
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

#print all except "Churros"
for favorite in favorites:
    if favorite == 'Churros':
        continue
    print("My favourite dessert is",favorite)
      
#prints only favorite dessert
for favorite in favorites:
    if favorite == 'Churros':
        print("My favourite dessert is",favorite)
        break    
else:
    print("your dessert is not found")    

