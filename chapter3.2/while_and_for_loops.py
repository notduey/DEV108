#!/usr/bin/env python3

#syntax of the while loop:
while boolean_expression:
    statements...

#a while loop that continues as long as the user enters "y" or "Y":
choice = "y"
while choice.lower() == "y":
    print("Hello!")
    choice = input("Say hello again? (y/n): ")
print("Bye!") #runs when loop ends


#a while loop that prints the numbers 0 through 4 to the console:
counter = 0
while counter < 5:
    print(counter, end=" ")
    counter += 1
print("\nThe loop has ended.")


#code that causes an infinite loop:
while True:
    #any statements in this loop runs forever
    #unless a break statement is executed as shown later below


#the syntax of for loop with the range() function:
for int_var in range_function:
    statements...


#the range function:
range(stop)
range(start, stop[, step])

#examples of the range() function:
range(5) #0, 1, 2, 3, 4
range(1,6) #1, 2, 3, 4, 5 (the first number is inclusive, the second number is exclusive)
range(2, 10, 2) #2, 4, 6, 8 (the number at the end in this case 2 is the step)
range(5, 0, -1) #5, 4, 3, 2, 1 (step number is -1 so the loop counts down)


#a for loop that prints the numbers 0 through 4:
for i in range(5):
    print(i, end=" ")
print("\nThe loop has ended.")


#a for loop that sums the numbers 1 throught 4:
sum_of_numbers = 0
for i in range(1,5):
    sum_of_numbers += i
print(sum_of_numbers) #result is 10


#a break statement that ecits an infinite while loop:
print("Enter 'exit' when you're done. \n")
while True:
    data = input("Enter an integer to square: ")
    if data == "exit":
        break #exits the loop
    i = int(data)
    print(i, "squared is", i * i, "\n")
print("Okay, bye!")


#a continue statement that jumps to the beginning of a while loop:
more = "y"
while more.lower() == "y":
    miles_driven = float(input("Enter miles driven: \t\t"))
    gallons_used = float(input("Enter gallons of gas used: \t"))

    #validate input
    if miles_driven <= 0 or gallons_used <= 0:
        print("Both entries must be greater than zero. Try again. \n")
        continue #jumps back to the beginning of the loop

    mpg = round(miles_driven / gallons_used, 2)
    print("Miles Per Gallon:", mpg, "\n")

    more = input("Continue? (y/n): ")
    print()

print("Okay, bye!")


#a for loop that calculates the future value of a one-time investment:
investment = 10000
for i in range(20):
    yearly_interest = investment * .05
    investment = investment + yearly_interest
investment = round(investment, 2)

#a while loop that gets the same result
year = 0
investement = 10000
while year < 20:
    yearly_interest = investment * .05
    investment = investment + yearly_interest
    year += 1
investment = round(investment, 2)


#a for loop that calulates the future value of a monthly investment:
monthly_investment = 100
monthly_interest_rate = .08 / 12
months = 120
future_value = 0
for month in range(months):
    future_value += monthly_investment
    monthly_interest_amount = future_value * monthly_interest_rate

    future_value += monthly_interest_amount
future_value = round(future_value, 2)


#nest loops that get the total of 3 valid test scores:
total_score = 0
for i in range(3):
    while True:
        score = int(input("Enter test score: "))
        if score >= 0 and score <= 100:
            total_score += score
            break
        else:
            print("Test scores must be from 0 - 100.")
print("Total score: ", total_score)


#the code for the test scores program
#!/usr/bin/env python3

#display a welcome message
print("The Test Scores Program")
print()
print("Enter 999 to end input.")
print("===============")

#initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = int(input("Enter test score: "))
    if test_score >0 and test_score <= 100:
        score_total += test_score
        counter += 1
    elif test_score == 999:
        break
    else:
        print("Test scores must be from 0 - 100. Try again.")

#calculate average score
average_score = round(score_total / counter)

#format and display the result
print("===============")
print("Total Score: " + score_total, "\nAverage Score: " + average_score)
print()
print("Bye!")


#the code for the Future Value Calculator:
#!/usr/bin/env python3

#display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    #get input from the user
    monthly_investment = float(input("Enter monthly investment: \t"))
    yearly_interest_rate = float(input("Enter yearly interest rate: \t"))
    years = int(intput("Enter number of years: \t\t"))

    #convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = year * 12

    #calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    #display the result
    print("Future value: \t\t\t" + str(round(future_value, 2)))
    print()

    #see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
