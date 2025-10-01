#!usr/bin/evr python3

#Python's arithmetic operators:
# + addition
# - subtraction
# * multiplication
# / division
# // integer (floor) division
# % modulo/remainder
# ** exponentiation

#examples with two operands
5 + 4 #result is 9
25 / 4 #result is 6.25
25 // 4 #result is 6
25 % 4 #result is 1
3 ** 2 #result is 9

#order of precedence/operations from highest to lowest:
#** (left to right)
#* / // % (left to right)
#+ - (left to right)

#examples that show the order of precedence and uses parentheses to change the order:
3 + 4 * 5 #result is 23 (the multiplication is done first
(3 + 4) * 5 #result is 35 (the addition is done first)


#code that calulates sales tax:
subtotal = 200.00
tax_percent = .05
tax_amount = subtotal * tax_percent #tax_amount is 10.0
grand_total = subtotal + tax_amount #grand_total is 210.0

#code that calculates the perimeter of a rectangle:
width = 4.25
length = 8.5
perimeter = 2 * (width + length) #perimeter is 25.5


#the most useful compound assignment operators:
# += addition assignment
# -= subtraction assignment
# *= multiplication assignment

#two ways to increment the number in a variable:
counter = 0
counter = counter + 1 #counter = 1
counter += 1 #counter = 2

#code that adds two numbers to a variable:
score_total = 0 #scoretotal = 0
score_total += 70 #scoretotal = 70
score_total += 80 #scoretotal = 150

#more compound assignment operator examples:
total = 1000.0
total += 100.0 #total is 1100.0

counter = 10
counter -= 1 #counter is 9

price = 100
price *= .8 #price is 80.0

#a floating point result that isn't precise: \
subtotal = 74.95 #subtotal is 74.95
tax = subtotal * .1 #tax is 7.495000000000001


#how to assign strings to variables:
first_name = "Bob" #Bob
last_name = 'Smith' #Smith
name = " " #empty string
name = "Bob Smith" #Bob Smith

#how to join three strings with the + operator:
name = last_name + ", " + first_name #name is "Smith, Bob"

#how to join a string and a number:
name = "Bob Smith"
age = 40
message = name + " is " + str(age) + " years old." #message is "Bob Smith is 40 years old."


#common escape sequences:
# \n newline
# \t tab
# \r return
#\" quotation mark in a double quoted string
#\' quotation mark in a single quoted string
#\\ backslash

#the new line character:
print("Title: Python Programming\nQuantity: 5")
#result:
#Title: Python Programming
#Quantity: 5

#the tab and new line characters:
print("Title:\t\tPython Programming\nQuantity:\t5")
#result:
#Title:          Python Programming
#Quantity:       5

#the backslahs in a windows path
print("C:\\murach\\python")
#result:
#C:\murach\python

#four ways to include quotation marks in a string:
print("Type \"x\" to exit.") #using the backslash
print('Type \'x\' to exit.') #using the backslash
print('Type "x" to exit.') #using different quotation marks
print("Type 'x' to exit.") #using different quotation marks

#implicit continuation of a string over serveral lines:
print("Total Score: "
      + str(score_total)
      + "\nAverage Score: "
      + str(average_score))

#the syntax of the print() function:
#print(data[, sep= ''][, end = '\n']) #this means that the sep and end parameters are optional
      
#three print() functions:
print(19.99) #prints 19.99
print("Price: ", 19.99) #prints Price: 19.99
print(1, 2, 3, 4) #prints 1 2 3 4

#two ways to get the same result:
print("Total Score: ", score_total, "\nAverage Score: ", average_score) #a print() function that receives four arguments

print("Total Score: " + str(score_total) + "\nAverage Score: " + str(average_score)) #a print() function that receives one string as the argument 

#the result for both: 
#Total Score:  240
#Average Score:  80

#examples that use the sep and end arguments:
print(1, 2, 3, 4, sep = ' | ') #prints 1 | 2 | 3 | 4
print(1, 2, 3, 4, end = ' !!! ') #prints 1 2 3 4 !!!


#the input() function:
input([prompt]) #the prompt parameter is optional

#code that gets string input from the user:
first_name = input("Enter your first name: ")
print("Hello " + first_name + "!")
#result if the user enters Mike:
#Enter your first name: Mike
#Hello Mike!

#another way to get iput from the user:
print("Enter your first name: ")
first_name = input()
print("Hello " + first_name + "!")
#result if the user enters Mike:
#Enter your first name:
#Mike
#Hello Mike!

#code that *attempts* to get numeric input:
score_total = 0
score = input("Enter your score: ")
score_total += score #causes a TypeError because score is a string

#three functions for working with numbers:
int(data)
float(data)
round(number[, ndigits]) #the ndigits parameter is optional

#codes that causes an exception:
x = 15
y = "5"
z = x + y #causes a TypeError because you can't add an integer and a string
#how using the int() function fixes the error:
x = 15
y = "5"
z = x + int(y) #z is 20

#code that gets an int value from the user:
quantity = input("Enter the quantity: ") #input is a string
quantity = int(quantity) #convert the string to an int
#how to use chaining to get the value in one statement:
quantity = int(input("Enter the quantity: ")) #input is converted to an int

#code that gets a float value from the user:
price = input("Enter the price: ") #input is a string
price = float(price) #convert the string to a float
#how to use chaining to get the value in one statement:
price = float(input("Enter the price: ")) #input is converted to a float

#code that uses the round() function:
miles_driven = 150
gallons_used = 5.875
mpg = miles_driven / gallons_used #mpg is 25.53191489361702
mpg = round(mpg, 2) #mpg is 25.53
#how to combine the last two statements:
mpg = round(miles_driven / gallons_used, 2)


