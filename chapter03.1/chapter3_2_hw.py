#!/usr/bin/env python3
"""
This program illustrates the use of the for/while loop and prints
all even numbers from 0-100 inclusively
"""
i = 0
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
        i += 2
