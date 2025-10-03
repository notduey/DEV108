#!/usr/bin/env python3
"""
This program illustrates the use of if statements
"""

print("Welcome!")
print()

birth_month = int(input("Enter the number of your birth month (1-12): "))

if (birth_month) >0 and (birth_month) <13:
    if birth_month == 1:
        print("Your birth month is January!")
    elif birth_month == 2:
        print("Your birth month is February!")
    elif birth_month == 3:
        print("Your birth month is March!")
    elif birth_month == 4:
        print("Your birth month is April!")
    elif birth_month == 5:
        print("Your birth month is May!")
    elif birth_month == 6:
        print("Your birth month is June!")
    elif birth_month == 7:
        print("Your birth month is July!")
    elif birth_month == 8:
        print("Your birth month is August!")
    elif birth_month == 9:
        print("Your birth month is September!")
    elif birth_month == 10:
        print("Your birth month is October!")
    elif birth_month == 11:
        print("Your birth month is November!")
    elif birth_month == 12:
        print("Your birth month is December!")
else:
    print("ERROR")
