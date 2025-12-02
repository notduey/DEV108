#!/usr/bin/env python
"""
This module contains 3 methods by the final
"""

def get_length(string):
    """
    This function returns the length of a string
    """
    length = len(string)
    return length

def get_string():
    """
    This function asks the user for a string
    """
    string = input("Enter a string: ")
    return string

def display_results(string, length):
    """
    This function prints the string and its length
    """
    print(f"String: {string}\nLength: {length}")
