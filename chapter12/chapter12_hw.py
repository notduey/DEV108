#!/usr/bin/env python
"""
This program reads from monthly_sales.txt file and saves it in a dictionary
and then asks the user for total, average, and highest annual sales
"""
import locale
locale.setlocale(locale.LC_ALL, "en_US")

def read_sales(file_name):
    """
    read from text file and saves it to dictionary
    """
    sales = {}
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                month, amount = line.split() #splits line i.e. july 1234
                #month = july, amount = 1234
                sales[month] = int(amount) #converts amount to int
        return sales
    except FileNotFoundError as e:
        print("File not found, error:", e)
        return {}
    except ValueError as e:
        print("Error:", e)
        return {}

def get_user_choice():
    """
    gets user choice
    """
    print("Press 1 for the total annual sales" \
    "\nPress 2 for the average annual sales" \
    "\nPress 3 for the month with the highest sales")
    choice = input("\nEnter your choice: ").strip()
    while True:
        try:
            choice = int(choice)
            if choice not in (1, 2, 3):
                choice = input("Input has to be 1, 2, or 3. Try again: ").strip()
            else:
                return choice
        except ValueError:
            choice = input("Input must be a number. Try again: ").strip()

def calculate_choice(choice, sales):
    """
    calculates total, average, or highest sales
    """
    total = sum(sales.values()) #sums all values in dictionary
    if choice == 1:
        formatted = locale.currency(total, grouping=True)
        print(f"\nThe total annual sales is {formatted}!")
    elif choice == 2:
        average = total / len(sales) #len(sales) is number of keys in dictionary
        formatted = locale.currency(average, grouping=True)
        print(f"\nThe average annual sales is {formatted}!")
    elif choice == 3:
        highest = max(sales, key=sales.get) #max function returns highest value
        #key=sale gets the key
        print(f"\nThe month with the highest sales is {highest}!")
    else:
        print("Invalid choice.")

def main():
    """
    calls every function
    """
    sales = read_sales("monthly_sales.txt")
    choice = get_user_choice()
    calculate_choice(choice, sales)

if __name__ == "__main__":
    main()
