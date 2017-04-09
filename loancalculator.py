def loan_calculator(amount, rate, time):
    total_amount = (amount * (rate/100) * time/12) + amount
    return total_amount

amount = int(input('enter the loan amount:'))
rate = int(input('enter the interest rate'))
time = int(input('enter time'))
print(loan_calculator(amount, rate, time))
