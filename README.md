# tax-calculator

imports needed:
pytest
typing

in order to run test delete the last line of code in main.py "run_checkout()"
re add if not running test


FUNCTIONS EXPLAINED

calculate_total_charge(state, records):

      This function takes in two parameters, state and records. state represents the state of the user and records represents a list of items the user wants to purchase. 
      The function calculates the total charge for the user's purchase, including sales tax. 
      It uses a dictionary tax_rates to look up the tax rate based on the user's state, and then calculates the tax for each item in records based on the item type and the tax rate. 
      Finally, it adds up the prices and taxes for each item to get the total charge and returns it.

populate_receipt(receipt_info):

    This function populates a list receipt_info with user inputs for item name, price, and type. It uses a while loop to repeatedly ask the user to enter information for a new item until the user enters "done". 
    For each item, it asks the user for a name, price, and type, and performs some error checking to make sure the price is a positive number and the type is valid.
    It then adds the item information to receipt_info and continues until the user enters "done". 
    Finally, it returns the populated  receipt_info list.

run_checkout(): 

     This function askS the user for their location (state abbreviation) and then populating a receipt with item information using 
     populate_receipt(). Once the receipt is populated, the function calculates the total charge using calculate_total_charge()
     and prints it out.
     The function also performs some error checking to make sure the user enters a valid state abbreviation.
