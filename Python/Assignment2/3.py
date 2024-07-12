'''
3. Write a programe to calculate the electricity bill (acept number of unit from user) acording to the
following criteria: Unit price for first 100 units No Charge, next 100 units Rs 5 rupees per unit, after 200
units Rs 10 rupees per unit
( For Example if units is 350 than total bill amount is Rs 3500)
'''

units = int(input("Enter the units consumed : "))
total_bill = 0
if units  <= 100 :
    total_bill = 0
elif units > 100 and units <= 200:
    total_bill = units * 5
elif units > 200:
    total_bill = units * 10 

print(f"Electricity Bill : {total_bill}")