#!/usr/bin/env python3

""" This is the module that you will import from your main program.
    You are free to change this file for any testing purpose you want. However,
    when I grade your paper I will use this exact unchanged file.
    Hence, your program must be able to function with this unchanged file.
    Also, no need to submit this file, since I have a copy of it.
"""

def show_food_menu():
    """This function only displays the menu"""
    print("Welcome to the General Fast Food")
    print("Press 1 to add pasta to your order $3")
    print("Press 2 to add salad to your order $6")
    print("Press 3 to add sandwich to your order $9")
    print("Press 0 if you don't want any food")

def show_drink_menu():
    """This function only displays the menu"""
    print("Welcome to the General Fast Food")
    print("Press 1 to add orange juice to your order $1")
    print("Press 2 to add water (free) to your order $2")
    print("Press 3 to add soda to your order $3")
    print("Press 0 if you don't want any drink")

def show_dessert_menu():
    """This function only displays the menu"""
    print("Welcome to the General Fast Food")
    print("Press 1 to add pie to your order $2")
    print("Press 2 to add cookies to your order $4")
    print("Press 3 to add fruit to your order $6")
    print("Press 0 if you don't want any dessert")

def get_user_choice():
    """This function reads the user choice and returns it
    Assume the user will always enter valid values"""
    choice = int(input("Choice: "))
    if choice not in (0, 1, 2, 3):
        raise ValueError("Choice must be 0, 1, 2, or 3.")
    return choice

def get_total_price(food_choice, drink_choice, dessert_choice):
    """Function calculates the prices
    you need to pass, as a parameter, the choices that the user made
    when ordering their food, drink and dessert
    """
    price = food_choice * 3 + drink_choice * 1 + dessert_choice * 2
    return price

def print_total_price(total_price):
    """this fucntion just prints a friendly message with the
    final price for the customer
    """
    print("Thanks for buying our food. Your bill is $", total_price)
