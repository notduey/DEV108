#!/usr/bin/env python3
"""
This program reads email_template.txt and emails.csv file 
then prints emails for each recipient by replacing {first_name} and {email}
"""
import csv

def main():
    """
    main function
    """
    #read email_template.txt
    with open("email_template.txt", "r", encoding="utf-8") as template:
        template = template.read() #read str

    #read emails.csv
    with open("emails.csv", "r", encoding="utf-8") as emails:
        reader = csv.reader(emails) #read csv

        for row in reader: #for loop that reads each row in csv file
            #assigns first name to first_name (first index of row)
            first_name = row[0].strip().title()
            #assigns email address to email (second index of row)
            email = row[2].strip()

            #replace {first_name} and {email}
            message = template.format(
                first_name = first_name,
                email = email
            )

            print(message) #prints message
            print()

if __name__ == "__main__":
    main()
