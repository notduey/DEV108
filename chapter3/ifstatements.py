#!/usr/bin/env python3

#the syntax of the if statement:
if boolean_expression:
    statements...

[elif boolean_expression:
    statements...
else:
    statements...]


#only an if clause:
if age >= 18:
    print("You may vote.")


#an if clause and an else clause:
if age >= 18:
    print("You may vote.")
else:
    print("You are too young to vote.")


#an if clause, two elif clauses, and an else clause:
if invoice_total >500:
    discount_percent = .2
elif invoice_total > 250:
    discount_percent = .1
elif invoice_total > 0:
    discount_percent = 0
else:
    print("Invoice total must be greater than zero.")


#the operation of an if statement:
#an if statement always contains an if clause, in addition, it may contain one or more elif clases and one else clause

#when an if statement is executed, the if clause is evaluated first, if it is true, the statements in this clause are executed and the if statement ends, otherwise, the first elif clause is executed

#if the statement in the elif clause is true, the statements in the clause are executed, otherwise, the next elif clause is evaluated, this continues until the condition in one of the elif clauses is true or the else clause is reached

#the statements in the else clause are exeuted if the conditions in all preceding clauses are false

#only one block of statements can be run for each time an if statement is executed


#an if statement used for grading:
score = int(input("Enter test score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F" 

#another way the if statement could be coded:
score = int(input("Enter test score: "))
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
elif score < 60:
    grade = "F"


#an if statement that validates the range of a score:
score = int(input("Enter test score: "))
if score >= 0 and score <= 100:
    total_score += score
else:
    print("Invalid score, must be 0 to 100.")


#an if statemetn that validates the customer type:
is_valid  = True
customer_type = input("Enter customer type (R/W): ")
if customer_type == "r" or customer_type == "w":
    pass #this statement does nothing, it is a placeholder
else:
    print("Invalid customer type, must be R or W.")
    is_valid = False


#nested if statements:
#discounts for retail customers
if customer_type.lower() == "r":
    if invoice_total < 100:
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = .1
    elif invoice_total >= 250:
        discount_percent = .2
#discounts for wholesale customers
elif customer_type.lower() == "w":
    if invoice_total < 500:
        discount_percent = .4
    elif incoice_total >= 500:
        discount_percent = .5
#all other customers
else:
    discount_percent = 0

#an if statement that gets the same results:
#discounts for retail customers
if customer_type.lower() == "r": and invoice_total < 100:
    discount_percent = 0
elif customer_type.lower() == "r" and invoice_total >= 100 and invoice_total < 250:
    discount_percent = .1
elif customer_type.lower() == "r" and invoice_total >= 250:
    discount_percent = .2
#discounts for wholesale customers
elif customer_type.lower() == "w" and invoice_total < 500:
    discount_percent = .4
elif customer_type.lower() == "w" and invoice_total >= 500:
    discount_percent = .5
#all other customers
else:
    discount_percent = 0


#code for the miles per gallon program:
#display a welcome message
print("The Miles Per Gallon Program")
print()

#get input from the user
miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))

if miles_driven <= 0:
    print("Miles driven must be greater than zero. Try again.")
elif gallons_used <= 0:
    print("Gallons of gas used must be greater than zero. Try again.")
else:
    #calculate miles per gallon
    mpg = round((miles_driven / gallons_used), 2) #the 2 at the end rounds to 2 decimal places
    print("Miles per gallon: ", mpg)

print()
print("Bye")


#another way the if statement could be coded:
if miles_driven > 0 and gallons_used > 0:
    mpg = round((miles_driven / gallons_used), 2)
    print("Miles per gallon: ", mpg)
else:
    print("Both entries must be greater than zero. Try again.")


#the code for the invoice program:
#!/usr/bin/env python3

#display a welcome message
print("The Invoice Program")
print()

#get user entries
customer_type = input("Enter customer type (r/w):\t") #\t adds a tab space
invoice_total = float(input("Enter invoice total:\t\t"))
print()

#determine discounts for retail customers
if customer_type.lower() == "r":
    if invoice_total > 0 and invoice_total <100:
        discount_percent = 0
    elif invoice_total >100 and invoice_total < 250:
        discount_percent = .1
    elif invoice_total >= 250 and invoice_total <500:
        discount_percent = .2
    elif invoice_total >= 500:
        discount_percent = .25
#determine discounts for Wholesale customers
elif customer_type.lower == "w":
    if invoice_total > 0 and invoice_total <500:
        discount_percent = .4
    elif invoice_total >= 500:
        discount_percent = .5
#set discount to zero if neither Retail or Wholesale
else:
    discount_percent = 0

#calculate discount amount and new invoice total
discount_amount = round(invoice_total * discount_percent, 2)
new_invoice_total = invoice_total - discount_amount

#display the results
print("Invoice total:\t\t" + str(invoice_total))
print("Discount percent:\t" + str (discount_percent))
print("Discount amount:\t" + str(discount_amount))
print("New invoice total:\t" + str(new_invoice_total))
print()
Print("Bye")