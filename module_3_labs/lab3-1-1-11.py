income = float(input("Enter the annual income: "))
max_income = 85528
tax = 0

if income < max_income:
    tax = income - (income / 100 * 18) - 556.02
    if tax < 0:
        tax = 0
else:
    tax_sum = income - 14839.02
    tax = tax_sum - (tax_sum / 100 * 32)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")