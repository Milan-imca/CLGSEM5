'''7
In an e-commerce application, create a function that accepts the number of items a customer wants
to purchase and checks if the stock is sufficient. Raise a StockError (custom exception) if the
requested quantity exceeds the available stock. Catch this exception and notify the user to adjust
their order.
'''



class StockError(Exception):
    pass


def purchase_items(available_stock):
    while True:
        try:

            quantity = int(input("Enter the number of items you want to purchase: "))
            
            
            if quantity > available_stock:
                raise StockError(f"Only {available_stock} items available. Please adjust your order.")
            
            print(f"Purchase successful! You ordered {quantity} item(s).")
            break 

        except StockError as e:
            print(e)  

        except ValueError:
            print("Invalid input. Please enter a valid number.")


available_stock = 10 
purchase_items(available_stock)
