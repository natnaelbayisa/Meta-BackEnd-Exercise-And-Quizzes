bil_total = 210

discount1 = 10
discount2 = 20

if bil_total >100 and bil_total < 200:
    bil_total -= discount1
    print("bill is greater than 100!")
elif bil_total > 200:
    bil_total -= discount2
    print("Bill is greater than 200")
else:
    print("bill is less than 100!")

print("Total bill is " + str(bil_total))