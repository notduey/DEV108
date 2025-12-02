#!/usr/bin/env python
"""
This module calls the functions from my_module
"""
import my_module as m

def main():
    """
    Main function
    """
    string = m.get_string()
    length = m.get_length(string)
    m.display_results(string, length)

if __name__ == "__main__":
    main()
