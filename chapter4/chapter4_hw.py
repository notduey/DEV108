#!/usr/bin/env python3
"""
This program calculates the final price of an order that contains bags of apples and bananas
"""

def get_number_fruits():
    """
    Asks user for number of fruits in bag, apple then banana
    """
    fruits = int(input("How many fruits are you buying?"))
    return fruits

def get_apple_price(apples):
    """
    Returns price of apples ($3 each)
    """
    price = apples * 3
    return price

def get_banana_price(bananas):
    """
    Returns price of bananas ($2 each)
    """
    price = bananas * 2
    return price

def print_bill(apple_total, banana_total):
    """
    Displays final bill and total
    """
    total = apple_total + banana_total
    print("You bought $" + banana_total, " of bananas and $" + apple_total, " of apples." \
    "\n Your final bill is $" + total + ".")
    print("Thank you for shopping with us")

def main():
    """
    Main function
    """
    apples = get_number_fruits()
    bananas = get_number_fruits()

    apple_total = get_apple_price(apples)
    banana_total = get_banana_price(bananas)

    print_bill(apple_total, banana_total)