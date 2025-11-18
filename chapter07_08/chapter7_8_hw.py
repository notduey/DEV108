#!/usr/bin/env python3
"""
This program calls function from hw_7_8_module and simulates
a user going to a fast food restaurant and ordering food
"""
import sys
import hw_7_8_module as hw

def main():
    """
    Main function calls other functions from hw_7_8_module and 
    prints the result to the console and prints a receipt to a file
    """
    try:
        #show menu
        hw.show_food_menu()
        food_choice = hw.get_user_choice()

        hw.show_drink_menu()
        drink_choice = hw.get_user_choice()

        hw.show_dessert_menu()
        dessert_choice = hw.get_user_choice()
    except ValueError as e:
        print("Error:", e, "\nNow exiting program.")
        sys.exit()

    #calculate total and print result
    total_price = hw.get_total_price(food_choice, drink_choice, dessert_choice)
    hw.print_total_price(total_price)


    #check if receipt file already exists
    filename = input("Enter filename to save your receipt: ")
    if not filename:
        print("Please enter a valid filename.\nNow exiting program.")
        sys.exit()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("File name already exists.\nNow exiting program.")
            sys.exit()
    except FileNotFoundError:
        pass #pass statement is used to ignore the error
    except OSError as e:
        print("File error:", e, "\nNow exiting program.")
        sys.exit()


    #write receipt to file
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Receipt\n")
            file.write(f"Food choice: {food_choice}")
            file.write(f"\nDrink choice: {drink_choice}")
            file.write(f"\nDessert choice: {dessert_choice}")
            file.write(f"\nTotal price: ${total_price}")
        print("Receipt saved to", filename, "sucessfully.")
    except OSError as e:
        print("File error:", e, "\nNow exiting program.")
        sys.exit()


if __name__ == "__main__":
    main()
