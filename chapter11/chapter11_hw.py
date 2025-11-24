#!/usr/bin/env python3
"""
This program calculates the difference between two datetime
"""
import sys
from datetime import datetime

def get_date(prompt):
    """
    Get a date from the user
    """
    date_string = input(prompt).strip()
    try:
        return datetime.strptime(date_string, "%m/%d/%Y at %H:%M")
    except ValueError as e:
        if "does not match format" in str(e):
            print("Invalid date format.\nNow Exiting program...")
        elif "out of range" in str(e):
            print(f"The date \"{date_string}\" doesn't exist.\nExiting program...")
        else:
            print(f"Error: \"{e}\"\nNow exiting program...")
        sys.exit()

first_date = get_date("Enter the first date (MM/DD/YYYY at HH:MM): ")
second_date = get_date("Enter the second date (MM/DD/YYYY at HH:MM): ")
print()

if first_date > second_date:
    print("The first date must be before the second date.\nNow exiting program...")
    sys.exit()

difference = second_date - first_date
days = difference.days
hours = difference.seconds // 3600 # 3600 seconds in an hour

DAY_LABEL = "day" if days == 1 else "days"
HOUR_LABEL = "hour" if hours == 1 else "hours"

print(f"The difference is {days} {DAY_LABEL} and {hours} {HOUR_LABEL}.")
