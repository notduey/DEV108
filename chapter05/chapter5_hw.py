#!/usr/bin/env python3
"""
This program calls function from hw_05_module and simulates
a user going to a fast food restaurant and ordering food
"""
import hw_05_module as hw

#show menu
hw.show_food_menu()
food_choice = hw.get_user_choice()

hw.show_drink_menu()
drink_choice = hw.get_user_choice()

hw.show_dessert_menu()
dessert_choice = hw.get_user_choice()

#calculate total and print result
total_price = hw.get_total_price(food_choice, drink_choice, dessert_choice)
hw.print_total_price(total_price)
