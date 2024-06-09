# Q1)
# Provided: balance, annualInterestRate, monthlyPaymentRate
# Find out credit card balance after 1 year
def annual_balance(balance, interest, monthlyRate=0.00, count=12):
    if count <= 0:
      return balance
    else:
      return annual_balance((balance * (1 - monthlyRate)) * (1 + interest), interest, monthlyRate, count - 1)
print("Credit Card Balance after 1 year:", annual_balance(balance, annualInterestRate / 12, monthlyPaymentRate))


# Q2) 
# Provided: balance, annualInterestRate
# Find minimum FIXED payment to pay off credit card debt in a year, multiples of 10
def minimum_payment(balance, interest, payment=0):
    def annual_balance(bal, rate, pay, count=12):
        if count <= 0:
            return bal
        else:
            return annual_balance(((bal - pay) * (1 + rate)), rate, pay, count - 1)
    if int(annual_balance(balance, interest, payment)) <=0 :
        return payment
    else:
        return minimum_payment(balance, interest, payment + 10)
print('Lowest Payment:', round(minimum_payment(balance, annualInterestRate / 12), 2))


# Q3) 
# Provided: balance, annualInterestRate
# Find minimum FIXED payment to pay off credit card debt in a year, by BISECTION SEARCH, to nearest cent
def minimum_payment(balance, interest, lower, upper):
    def annual_balance(bal, rate, pay, count=12):
        if count <= 0:
            return bal
        else:
            return annual_balance(((bal - pay) * (1 + rate)), rate, pay, count - 1) 
    pay = (lower + upper) / 2
    if int(annual_balance(balance, interest, pay)) > 0 :
        return minimum_payment(balance, interest, pay, upper)
    elif int(annual_balance(balance, interest, pay)) <= -0.12 :
        return minimum_payment(balance, interest, lower, pay)
    else:
        return pay
print('Lowest Payment:', round(minimum_payment(balance, annualInterestRate / 12, 0, balance), 2))
