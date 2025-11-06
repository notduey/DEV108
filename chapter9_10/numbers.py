#!/usr/bin/env python3

#two numeric data types:
int # 4 bit, integer s from -2,147,483,648 to 2,147,483,647
float #8 bit, floating point numbers from -1.7976931348623157e308 to 1.7976931348623157e308

#example of float values:
21.5 #negative float value
-124.82 #negative float value
-3.7e-9 #float notation for -0.000000037

#variables that are set with scientific notation
value1 = 2.382E+5 #2.382 * 10^5 (238200)
value2 = 3.25E-8 #3.25 * 10^-8 (0.0000000325)


#example of a floating-point error:
balance = 100.10
balance += 100.10
balance += 100.10
print("Balance =", balance)
#console result: Balance = 300.299999999999995

#code that fixed the floating-point error
balance = round(balance, 2) #rounds to the second decimal place
print("Balance =", balance)
#console result: Balance = 300.3


#common functions of math module
pow(num, pow) #num raised to the power of pow
sqrt(num) #square root of num
ceil(num) #smallest integer greater than or equal to num
floor(num) #largest integer less than or equal to num

#constant of math module
pi


#importing math module
import math

#pow() and sqrt() functions
result = m.pow(2, 3) # 8.0 (the cube of 2)
result = m.sqrt(16) # 4.0 (square root)
result = m.pow(125, 1/3) # 4.999999999999999 (cube root)

#the pi constant
radius = 12
circumference = m.pi * radius * 2 #75.39822368615503
area = m.pi * m.pow(radius, 2) # 452.3893421169302
area = m.pi * radius**2 # 452.3893421169302

#floor() and ceil() function
result = m.floor(12.545) # 12
result = m.ceil(12.545) # 13
result = m.floor(-3.432) # -4
result = m.ceil(-3.432) # -3

#the ceil() function with decimal places
m.ceil(2.0083) # 3
m.ceil(2.0083 * 10) / 10 # 2.1
m.ceil(2.0083 * 100) / 100 # 2.01

#the floor() function with decimal places
m.floor(2.0083) # 2
m.floor(2.0083 * 10) / 10 # 2.0
m.floor(2.0083 * 1000) / 1000 # 2.008


#syntax for string format() method
"{:format_specification}...".format(data_item...)

#The syntax for the format specification
[field_width][comma][.decimal_places][type_code]


#common type codes
d Integer
f Floating-point number
% Percent
e Scientific notation

#the format() method
fp_number = 12345.6789
print("{:.2f}".format(fp_number)) #12345.68 (2 decimal places)
print("{:.4f}".format(fp_number)) #12345.6789 (4 decimal places)
print("{:,.2f}".format(fp_number)) #12,345.68 (2 decimal places, the comma is added to separate thousands)

print("{:15,.2f}".format(fp_number)) #12,345.68 
#: → starts the format specification.
#15 → sets the field width to 15 characters, meaning the number will take up 15 spaces total and be right-aligned (useful for column alignment).
#, → adds commas as thousand separators (e.g., 12,345.68).
#.2f → formats the number as a floating-point value with two decimal places.

int_number = 12345
print("{:d}".format(int_number)) # 12345 d is for integer
print("{:,d}".format(int_number)) # 12,345 d is for integer, with comma to separate thousands

fp_number = .12345
print("{:.0%}".format(fp_number)) # 12% (0 decimal places, % turns it into a percentage)
print("{:.1%}".format(fp_number)) # 12.3% (1 decimal place, % turns it into a percentage)

fp_number = 12345.6789
print("{:.2e}".format(fp_number)) # 1.23e+04 (2 decimal places, e turns it into scientific notation)
print("{:.4e}".format(fp_number)) # 1.2346e+04 (4 decimal places, e turns it into scientific notation)


#how to use field widths to align results
print("{:15} {:>10} {:>5}".format("Description",
"Price", "Qty")) 
#{:15} Use 15 spaces, left-aligned by default. Perfect for longer text like “Description.”
#{:>10} Use 10 spaces, right-aligned (because of >).
#{:>5} Use 5 spaces, right-aligned.

print("{:15} {:10.2f} {:5d}".format("Hammer", 9.99, 3))
#{:10.2f} Use 10 spaces, right-aligned, with 2 decimal places.
#{:5d} Use 5 spaces, right-aligned, d is for integer.
print("{:15} {:10.2f} {:5d}".format("Nails", 14.5, 10))
#the console results:
Description     Price       Qty
Hammer          9.99        3
Nails           14.50       10


#commonly used functions of the locale module
setlocale(category, locale)
currency(num[, grouping])
format(format, num[,grouping])

#codes for working with locales
English/United States: us or en_US #currency format: $12,345.67
English/United Kingdom: uk or en_UK #currency format: £12,345.67
German/Germany: de or de_DE #currency format: +12.345,67€

#how to import local module into the lc namespace
import locale as lc

#how to set the locale to English/United States
lc.setlocale(lc.LC_ALL, "us") #works with Windows
lc.setlocale(lc.LC_ALL, "en_US") #works with macOS and Linux

#how to set the locale on most systems
results = lc.setlocale(lc.LC_ALL, "") #works with Windows
if result == "C" or result.startswith("C/"): #if 'C' or 'C/' is returned
    lc.setlocale(lc.LC_ALL, "en_US") #set default locale, works with macOS and Linux


#currrency() function
print(lc.currency(12345.15, grouping=True)) #$12,345.15 (grouping=True adds commas to separate thousands)

#format() function
print(lc.format("%d", 12345, grouping=True)) # 12,345 (grouping=True adds commas to separate thousands, %d is for integer)
print(lc.format("%.2f", 12345.15, grouping=True)) # 12,345.15 (2 decimal places, grouping=True adds commas to separate thousands, %.2f is for floating-point number)



#The user interface for the Invoice program with INCORRECT results
Enter order total:      100.05
Order total:            100.05
Discount amount:        10.01
Subtotal:               90.05
Sales tax:              4.50
Invoice total:          94.55

#The code that yields incorrect results
order_total = float(input("Enter order total: "))
print()

# determine discount percent
if order_total > 0 and order_total < 100:
    discount_percent = 0
elif order_total >= 100 and order_total < 250:
    discount_percent = .1
elif order_total >= 250:
    discount_percent = .2

# calculate the results
discount = order_total * discount_percent
subtotal = order_total - discount
sales_tax = subtotal * .05
invoice_total = subtotal + sales_tax

# display the results
print("Order total: {:10,.2f}".format(order_total))
print("Discount amount: {:10,.2f}".format(discount))
print("Subtotal: {:10,.2f}".format(subtotal))
print("Sales tax: {:10,.2f}".format(sales_tax))
print("Invoice total: {:10,.2f}".format(invoice_total))
print()


#the code that FIXES this problem
#calculate results with rounding
discount = round(order_total * discount_percent, 2)
subtotal = order_total - discount
sales_tax = round(subtotal * .05, 2)
invoice_total = subtotal + sales_tax

#The user interface for the Invoice program with correct results
Enter order total:      100.05
Order total:            100.05
Discount amount:        10.01
Subtotal:               90.04
Sales tax:              4.50
Invoice total:          94.54
Continue? (y/n):


#how to create Demical object and use them in calculations
from decimal import Decimal

order_total = Decimal("100.05")
discount_percent = Decimal(".1")
discount = order_total * discount_percent # 10.005
subtotal = order_total - discount # 90.045
tax_percent = Decimal(".05")
sales_tax = subtotal * tax_percent # 4.50225
invoice_total = subtotal + sales_tax # 94.54725
test1 = subtotal * 2 # Legal. You can mix Decimal and int
test2 = subtotal * 3.5 # Error! You can't mix Decimal and float


#syntax of quantize() method of Decimal object
object.quantize(Decimal("positions_code")[,
rounding_constant])

#Three of the rounding constants
ROUND_HALF_UP
ROUND_HALF_DOWN
ROUND_HALF_EVEN

#How to specify the number of decimal places
discount = Decimal("10.005")
discount = discount.quantize(Decimal("1.00")) #1.00 means round to 2 decimal places, result is #10.00

#How to override the default rounding mode from decimal import ROUND_HALF_UP
discount = Decimal("10.005")
discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP) # ROUND_HALF_UP means round up, result is 10.01



#code for the invoice program
from decimal import Decimal
from decimal import ROUND_HALF_UP

choice = "y"
while choice == "y":

    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"),
    ROUND_HALF_UP)
    print()

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    subtotal = order_total - discount
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"),
    ROUND_HALF_UP)

    invoice_total = subtotal + sales_tax

    # display the results
    print("Order total: {:10,}".format(order_total))
    print("Discount amount: {:10,}".format(discount))
    print("Subtotal: {:10,}".format(subtotal))
    print("Sales tax: {:10,}".format(sales_tax))
    print("Invoice total: {:10,}".format(invoice_total))
    print()

    choice = input("Continue? (y/n): ")
    print()

print("Bye")



#user interface for the Future Value Program
Enter monthly investment:   100
Enter yearly interest rate: 12.5
Enter number of years:      10

Monthy investment:      $100.00
Interest rate:             12.5
Years:                       10
Future value:        $23,938.13

Continue? (y/n):

#code for the Future Value Program
from decimal import Decimal
import locale as lc

def get_future_value(monthly_investment, yearly_interest, years):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12
    future_value = Decimal("0.00")
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    future_value = future_value.quantize(Decimal("1.00"))
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # convert user input to Decimal and int values
        monthly_investment = Decimal(input("Enter monthly investment: "))
        yearly_interest = Decimal(input("Enter yearly interest rate: "))
        years = int(input("Enter number of years: "))
        future_value = get_future_value(monthly_investment, yearly_interest, years)
        print()

        # format and display the results
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C" or result.startswith("C/"):
            lc.setlocale(lc.LC_ALL, "en_US")
        line = "{:20} {:>10}"
        print(line.format("Monthy investment:", lc.currency(monthly_investment, grouping=True)))
        print(line.format("Interest rate:", yearly_interest))
        print(line.format("Years: ", years))
        print(line.format("Future value:", lc.currency(future_value, grouping=True)), "\n")
            
        choice = input("Continue? (y/n): ")
        print()

if __name__ == "__main__":
    main()