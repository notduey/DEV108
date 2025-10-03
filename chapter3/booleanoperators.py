#!/usr/bin/env python3

#rational operators:
#== equal to
#!= not equal to
#< less than
#> greater than
#<= less than or equal to
#>= greater than or equal to


#boolean expressions:
age == 5 #variable equal to numeric literal
first_name == "John" #variable equal to string literal

quantity != 0 #variable not equal to numeric literal

distance > 5.6 #variable greater than numeric literal
fuel_req < fuel_cap #variable less than variable

distance >= limit #variable greater than or equal to variable
stock <= reorder_point #variable less than or equal to variable

rate / 100 >= 0.1 #expression greater than or equal to numeric literal


#how to assign a boolean value to a variable:
active = True #variable is set to boolean true value
active = False #variable is set to boolean false value


#logical operators with order of precedence:
#1. not
#2. and
#3. or


#boolean expressions that use logical operators:
age >= 65 and city == "Chicago" #the AND operator, both expressions must be true

city == "Greenville" or age >= 65 #the OR operator, only or at least one expression must be true

not age >= 65 #the NOT operator, negates the expression

age >= 65 and city == "Greenville" and state == "SC" #multiple AND operators

age >= 65 or age <= 18 or status == "retired" #multiple OR operators

(age >= 65 and status == "retired") or age <18 #combined AND and OR operators with parentheses to change order of precedence

age >= 65 and (status == "retired" or state == "SC") #combined AND and OR operators with parentheses to change order of precedence


#some string comparisons:
"apple" < "Apple" #False, lowercase letters have higher ASCII values than uppercase letters

"App" < "Apple" #True, shorter strings are less than longer string strings if all characters in the shorter string match the beginning of the longer string

"1" < "5" #True, string comparison is based on ASCII values
"10" < "5" #True, string comparison is based on ASCII values, first character "1" is less than "5"


#the sort sequence of digits and letters:
#digits from 0 to 9
#uppercase letters from A to Z
#lowercase letters from a to z


#two string method:
lower() #returns a copy of the string with all lowercase letters
upper() #returns a copy of the string with all uppercase letters

#how to call a string method:
variableName.methodName()

#how to compare strings with the lower() method:
string1 = "Mary"
string2 = "mary"

string1 == string2 #False, because the uppercase "M" is not equal to the lowercase "m"
string1.lower() == string2.lower() #True, because both strings are converted

print(string1) #prints "Mary"
print(string2) #prints "mary"


#how the lower() method can simplify code:
#without the lower() method:
customer_type = "r" or customer_type = "R"

#with the lower() method:
customer_type.lower() == "r"

