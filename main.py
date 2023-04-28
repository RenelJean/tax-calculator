from typing import Union


def calculate_total_charge(state: str, records: list[dict[str, Union[str, float]]]) -> float:
    """
    Calculates the total charge for a customer at checkout, including sales tax.
    Takes the user's state and a list of items to be purchased.
    """
    tax_rates = {
        'DE': 0.0,
        'NJ': 0.066,
        'PA': 0.06
    }

    total = 0.0
    for record in records:
        item_type = record['type']
        price = float(record['price'])

        # Calculate tax
        tax_rate = tax_rates[state]

        if item_type == 'wic eligible food':
            tax_rate = 0.0
        elif item_type == 'clothing':
            if state == 'PA':
                tax_rate = 0.0
            elif state == 'NJ' and 'fur' not in record['name'].lower():
                tax_rate = 0.0

        tax = price * tax_rate

        # Add price and tax to total
        total += price + tax

    return round(total, 2)


def populate_receipt(receipt_info):
    """
    Populates the receipt with user inputs for item name, price and type
    """
    while True:
        choice = input("Enter 'done' to finish adding items or any other key to continue: ")
        if choice.lower() == "done":
            break
        name = input("Enter the item name: ")
        price = input("Enter a positive price: ")
        try:
            price = float(price)
            if price <= 0:
                print("Error: price must be a positive number")
                continue
        except ValueError:
            print("Error: price must be a positive number")
            continue
        item_type = input("Enter a type (Wic Eligible food, Clothing, Electronic, Fur): ")
        if item_type.lower() not in ["wic eligible food", "clothing", "electronic", "fur"]:
            print("Error: invalid item type")
            continue
        data = {"name": name, "price": price, "type": item_type.lower()}
        receipt_info.append(data)

    return receipt_info


def run_checkout():
    """
    Runs the checkout process by asking user for location and populating receipt
    """
    receipt = []  # Initialize receipt list
    populate_receipt(receipt)
    while True:
        choice = input("Enter 'done' to calculate purchase total: ")
        if choice.lower() == "done":
            break

    location = input("Enter your state abbr (DE,PA,NJ): ")
    if location.upper() not in ["DE", "PA", "NJ"]:
        print("Error please enter one of the following: [PA,DE,NJ]")
    else:
        if receipt:
            purchase_total = calculate_total_charge(location, receipt)
            print(purchase_total)
        else:
            print("Error: List is empty")


run_checkout()
