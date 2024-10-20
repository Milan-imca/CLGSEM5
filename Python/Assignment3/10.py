'''
  10 Write a function calculate_discount(price, discount=0.10, *, tax_rate) that calculates the
  final price after applying a discount and a tax. The tax rate is a required keyword argument.
'''

def calculate_discount(price, discount=0.10, *, tax_rate):
    discounted_price = price * (1 - discount)
    final_price = discounted_price * (1 + tax_rate)
    return final_price

# Example usage:
print(calculate_discount(100, tax_rate=0.07))
