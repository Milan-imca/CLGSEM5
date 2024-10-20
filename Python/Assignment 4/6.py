'''6
In a flight booking system, write a function that accepts user input for seat selection (like "A5",
"B7", etc.). Raise a ValueError if the user enters an invalid seat format (e.g., "5A" or "Z99").
Handle the exception and prompt the user to enter a valid seat number.
'''

import re

def seat_selection():
    while True:
        try:
            seat = input("Please enter a seat (e.g., A5, B7): ").upper()
            if not re.match(r'^[A-H][1-9]\d?$', seat): 
                raise ValueError("Invalid seat format. Seat must be a letter followed by a number.")
            
            print(f"Seat {seat} selected successfully.")
            break 

        except ValueError as e:
            print(e) 


seat_selection()
