#!/usr/bin/env python3

#goal of testing:
#to FIND all errors before the program is put into production

#the goal of debugging: 
#to FIX all errors before the program is put into production

#three types of errors:
#SYNTAX errors violate python syntax rules for coding. These are also called copile-time errors, and are caught by IDLE and python compiler before you run the program.
#RUNTIME errors don't violate the syntax, but they throw exceptions that stop the program from continuing to run. Many of these exceptions are due to programming errors that need to be fixed. Some exceptions need to be handled by the program so the the program doesn't crash.
#LOGIC errors are statements that don't cause syntax or runtime errors, but produce the wrong results. Your code could run perfectly but might have the wrong outcome.


#python function that contains errors:
def calculate_future_value(monthly_investment, yearly_interest, years):
# convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months)
        future_value += monthly_investment_amount #monthly_investment_amount isn't defined, meaning it we haven't assigned a value to it
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

#Common syntax errors:
#misspelling keywords
#forgetting the colon at the end of the opening line of a function definition, if clause, else clause, while statement, for statement, try clause, or except clause
#forgetting an opening or closing quotation mark or parentheses
#using parentheses when you should be using brackets, or vice versa
#improper indentation


#problems with names and values:
#misspelling or incorrectly capitalizing a variable or function name
#using a keyword as a variable or function name
#not checking that a value is the right date type before processing it. For example using a number when it needs to be converted to a string, or vice versa


#problem with floating-point arithmetic:
#the float data type in python uses floating-point numbers, and that can lead to arithemtic results that are imprecise. For example:

sales_amount = 74.95;
discount = sales_amount * .1 #result is 7.495000000000001

#one way to fix this problem is to round the result to the right number of decimal places. If necessary, you can also convert it back to a floating-point number:

discount = round(discount, 2)   #result is 7.5

#another way to fix this problem is to use the standard decimal module, which lets you work with decimal numbers instead of floating-point numbers


#two critical test phases:
#1. test the program with valid input data to make sure the results are correct
#2. test the program with invalid data or unexpected user actions. Try everything you can think of to make the program fail

#how to make a test plan for the critical phases:
#1. list all valid entries that you're going to make and the correct results for each set of entries. Then make sure that the results are correct when you test with these entries.
#2. list the invalid entries that you're going to make. These should include entries that test the limits of the allowable values.

#two common testing problems:
#not testing a wide enough range of entries
#not knowing what the results of eah set of entries should be and assuming that the answers are correct because they look correct