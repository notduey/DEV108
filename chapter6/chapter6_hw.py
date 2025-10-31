#!usr/bin/env python3
"""
This program gets the average value of X amount of numbers the user inputs
"""

def get_list_size():
    """
    code that asks the user how many numbers they want to enter
    """
    list_size = int(input("How many numbers do you have? "))
    return list_size

def get_numbers(list_size, user_list):
    """
    code that gets the numbers from the user
    """
    for number in range(list_size):
        number = int(input("Enter a number: "))
        user_list.append(number)
    return user_list

def get_sum(user_list):
    """
    code that gets the sum of the numbers the user entered
    """
    number_sum = 0
    for i in user_list:
        number_sum += i
    return number_sum

def get_average(number_sum, user_list):
    """
    code that gets the average of the numbers the user entered
    """
    average = number_sum / len(user_list)
    return average

def main():
    """
    main function that calls the other functions
    """
    user_list = []
    list_size = get_list_size()
    get_numbers(list_size, user_list)
    print("You typed, ", user_list)
    number_sum = get_sum(user_list)
    average = get_average(number_sum, user_list)
    print("sum: ", number_sum)
    print("Average: ", round(average, 1))
