#!usr/bin/env python3

#Code that can cause a ValueError exception
number = int(input("Enter an integer: "))
print("You entered a valid integer of " + str(number) + ".")
print("Thanks!")

#The console for a valid integer
Enter an integer: 5
You entered a valid integer of 5.
Thanks!

#The console for an invalid integer
Enter an integer: five
Traceback (most recent call last):
    File "C:\murach\python\book_figs\ch07\fig1.py", line 1, in <module>
        number = int(input("Enter a valid integer: "))
ValueError: invalid literal for int() with base 10: 'five'


#two functions that can cause a ValueError exception:
int(data) #can't convert data argument into an int value
float(data) #can't convert data argument into a float value


#syntax for try statement that catches an exception
try:
    statements
except: [ExceptionName]:
    statements


#how to handle a ValueError exception
try: #runs the code and tries to convert the input into an int
    number = int(input("Enter an integer: "))
    print("You entered a valid integer of " + str(number) + ".")
except ValueError: #catches the ValueError exception
        print("You entered an invalid integer. Please try again.")
print("Thanks!")

#The console for a valid integer
Enter an integer: 5
You entered a valid integer of 5.
Thanks!

#The console for an invalid integer
Enter an integer: five
You entered an invalid integer. Please try again.
Thanks!


#how to handle all exceptions
try:
    number = int(input("Enter an integer: "))
    print("You entered a valid integer of " + str(number) + ".")
except: #catches all exceptions
    print("You entered an invalid integer. Please try again.")
print("Thanks!")



#The code for the Total Calculator program
def get_price():
    while True: #the while statement runs until the input is valid
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Total Calculator program\n")
    # get the price and quantity
    price = get_price()
    quantity = get_quantity()
    # calculate the total
    total = price * quantity
    # display the results
    print()
    print("PRICE: ", price)
    print("QUANTITY: ", quantity)
    print("TOTAL: ", total)

if __name__ == "__main__":
    main()



#hierarchy for five common exceptions
Exception
    OSError
        FileExistsError
        FileNotFoundError
    ValueError
#the higher level exceptions are handled by the lower level exceptions, meaning that they are caught by the lower level exceptions before they are caught by the higher level exceptions


#the syntax for a try statement with multiple except blocks
try:
    statements
except ExceptionName:
    statements
except ExceptionName:
    statements


#code that handles multiple exceptions
filename = input("Enter filename: ")
movies = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError:
    print("Could not find the file named " + filename)
except OSError:
    print("File found - error reading file")
except Exception:
    print("An unexpected error occurred")
#The console when a FileNotFoundError occurs
Could not find the file named films.txt
#The console when an OSError occurs
File found – error reading file
#The console when any other Exception occurs
An unexpected error occurred.


#built-in type() function
type(object)

#the exit() function of the sys module
exit()


#the complete syntax for the except clause
except [ExceptionName] [as name]:
    statements

#code that handles multiple exceptions
import sys

filename = input("Enter filename: ")
movies = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
    sys.exit()
except OSError as e:
    print("OSError:", e)
    sys.exit()
except Exception as e:
    print(type(e), e)
    sys.exit()
#The console when a FileNotFoundError occurs
FileNotFoundError: [Errno 2] No such file or directory: 'films.txt'
#The console when an OSError occurs
OSError: [Errno 2] No such file or directory: 'films.txt'
#The console when any other Exception occurs
<type 'exceptions.Exception'> [Errno 2] No such file or directory: 'films.txt'



#code for movie list 2.0 program
import csv
import sys

FILENAME = "movies.csv"

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except Exception as e:
        print(type(e), e)
        exit_program()

def exit_program():
    print("Terminating program.")
    sys.exit()

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number." +
                  "Please try again.")
        else:
            break
movie = movies.pop(number - 1)
write_movies(movies)
print(movie[0] + " was deleted.\n")

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")



#complete syntax for a try statement
try:
    statements
except [ExceptionName] [as name]:
    statements
except [ExceptionName] [as name]:
    statements
finally: #finally clause is to clean up resources
    statements


#a function that uses. a with statement to clean up resources:
def read_movies(filename):
    try:
        with open(filename, newline"") as file:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except Exception as e:
        print(e)


#a function that uses a finally clause to clean up resources
def read_movies(filename):
    try:
        file = open(filename, newline="")
        try:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
            return movies
        except Exception as e:
            print(type(e), e)
        finally:
            file.close()
    except FileNotFoundError as e:
        print(e)


#the syntax for the raise statement
raise ExceptionName("Error message")

#raising a ValueError exception
raise ValueError("Error message")


#raising an excpeption for testing an excpetion handler
def get_movies(filename):
    try:
        with open(filename, newline="") as file:
            raise OSError("OSError") # for testing
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except Exception as e:
        print(type(e), e)


#raising an exception that should be handled by the calling function
def get_movies(filename):
    if len(filename) == 0:
        raise ValueError("The filename argument is required.")
    with open(filename, newline="") as file:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
            return movies
    


#logging and exception and raising it for the calling function
def get_movies(filename):
    try:
        with open(filename, newline="") as file:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except Exception as e:
        log_exception(e)
        raise e
