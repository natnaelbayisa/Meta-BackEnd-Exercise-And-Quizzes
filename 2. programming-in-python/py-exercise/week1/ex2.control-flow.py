loyalty_customer = True
total_bill = float(input("Enter your total bill: " ))

#apply 20% discount
if loyalty_customer and total_bill > 100:
    total_bill -= (float(total_bill)/100) * 20
#apply 10% discount
elif total_bill > 100:
    total_bill -= (float(total_bill)/100) * 10
#no discount for 5% 
else:
    print("Sorry no dicount for you!")

print("" + str(total_bill))