
# bill = 175.00

# tax_rate = 15

# total_tax = (bill*tax_rate)/100.00

# print("Total Tax", total_tax)


def calculateTax(bill, tax_rate):
    return (bill*tax_rate)/100.00

print("Total tax", calculateTax(175.00,15))
print("Total tax", calculateTax(200.00,20))