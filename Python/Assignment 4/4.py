'''4
Write a function that calculates the interest rate for a savings account. The interest is calculated as
interest = (balance * rate) / months. Use try-except to handle the case where the number of months
is zero, which would raise a ZeroDivisionError.
'''

def calculate_interest(balance, rate, months):
    try:
        interest = (balance * rate) / months
        return interest
    except ZeroDivisionError:
        return "Error: Number of months cannot be zero."


balance = 1000  
rate = 0.05     
months = 0      

interest = calculate_interest(balance, rate, months)
print(interest)
