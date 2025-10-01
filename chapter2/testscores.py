#!usr/bin/env python3

#This is a tutorial program that illustrates the use of 
#the while and if statements

#initialize variables
counter = 0
score_total = 0
test_score = 0

#get scores
while test_score != 999:
    test_score = int(input("Enter test score:"))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score   #add score to total
        counter += 1                #add 1 to counter

#calculate average score
average_score = round(score_total / counter)

print("Total Score: " + str(score_total))
print("Average Score: " + str(average_score))

#this would be an indentation error:

#print("Total Score: " + str(score_total))
#   print("Average Score: " + str(average_score))

#Two ways to continue one statement over two or more lines:

#Implicit continuation
print("Total Score: " + str(score_total)
      + "\nAverage Score: " + str(average_score))

#Explicit continuation
print("Total Score: " + str(score_total) \
      + "\nAverage Score: " + str(average_score))

#Python relies on proper indentation. Incorrecti indentation causes an error.
#The standard indentation is four spaces.

#With implicit continuation, you can divde statements after parentheses, brackets, and braces, and before or after operators like plus or minus signs.

#With explicit continuation, you can use the backslash \ character to divde statements anywher in a line