#!/usr/bin/env python3

#three python date types: string, integer, float
first_name = "Mike" #sets string "Mike"
quantity1 = 3   #sets integer 3
quantity2= 5  #sets integer 5
list_price = 19.99 #sets float 19.99

#code that assigns new data to the variables above
first_name = "Joel" #sets string "Joel"
quantity1 = 10  #sets integer 10
quantity1 = quantity2 #sets integer 5 (same as quantity2)
quantity1 = "15" #sets string "15"

#code that causes an error due to incorrect case
#quantity1 = Quantity2 #causes NameError because Quantity2 is not defined


#to code a literal value for a string, enclose the value in single or double quotes. This is called a string literal.
literal_string1 = "100" #string literal

#to code a literal value for a number, code the number without quotes. This is called a numeric literal.
literal_integer1 = 100 #integer literal
literal_float1 = 99.99 #float literal

#rules for naming variables:
#a variable name must begin with a letter or an underscore
#a variable name can't contain spaces, puntuation, or special characters other than underscores
#a veriable name can't begin with a number, but can use numbers after the first character
#a varible name can't be the same as a keyword that's reserved by Python

#Python keywords:
#and as assert break class continue def del elif else escept False finally for from global if import in is lambda None nonlocal not or pass raise return True try while with yield

#Two naming styles for variables:
varible_name = "underscore notation" #underscore notation
variableName = "camel case" #camel case notation

#Start all variable names with a lowercase letter
#Use underscore notation or camel case
#Use meaningful names that are easy to remember
#Don't use the names of built-in functions, such as print()
