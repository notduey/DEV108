#!usr/bin/env python3

#two types of files in python:
#text files
#binary files

#sequence of file operations:
#1. open the file
#2. write data to the file or read data from the file
#close the file


#open() function:
open(file, mode)

#modes:
#r - open file for reading
#w - open file for writing, writing means overwriting the file
#a - open file for appending, appending means adding data to the fil
#b - open file in binary mode

#close() method:
close()


#how to opne a file in write mode and close file manually:
outfile = open("test.txt", "w")
outfile.write("Test")
outfile.close()


#How to use with statements to open and close files
#The syntax of the with statement for file I/O
with open(file, mode) as file_object:
    statements...
#Code that opens a text file in write mode and automatically closes it
with open("test.txt", "w") as outfile:
    outfile.write("Test")
#Code that opens a text file in read mode and automatically closes it
with open("test.txt", "r") as infile:
    print(infile.readline())


#write() method of a file object:
write(str)

#how to write one line to a text file
with open("members.txt", "w") as file:
    file.write("John Cleese\n")

#how to append one line to a text file
with open("members.txt", "a") as file:
    file.write("Eric Idle\n")


#3 read methods of a file object
read() # reads the entire file
readline() # reads a single line
readlines() # returns a list of lines


#how to use a loop to read each line of the file
with open("members.txt", "r") as file:
    for line in file:
        print(line, end="")
    print()

#how to read the entire file as a string
with open("members.txt") as file:
    content = file.read()
    print(content)

#how to read the entire file as a list
with open("members.txt") as file:
    members = file.readlines();
    print(members[0], end="")
    print(members[1])

#how to read each line of the file
with open("members.txt") as file:
    member1 = file.readline();
    print(member1, end="")
    member2 = file.readline();
    print(member2)

#how to write and read a list of strings
#How to write the items in a list to a file
members = ["John Cleese", "Eric Idle"]
with open("members.txt", "w") as file:
    for m in members:
        file.write(m + "\n") # adds new line

#How to read the lines in a file into a list
members = []
with open("members.txt") as file:
    for line in file:
        line = line.replace("\n", "") # removes new line
        members.append(line)
print(members)
#The result that’s printed to the console: ['John Cleese', 'Eric Idle']

#How to write and read a list of numbers
#How to write the items in a list to a file
years = [1975, 1979, 1983]
with open("years.txt", "w") as years_file:
    for year in years:
        years_file.write(str(year) + "\n") # converts int to str
#How to read the items in a list from a file
years = []
with open("years.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        years.append(int(line)) # converts str to int
print(years)
#The result that’s printed to the console: [1975, 1979, 1983]



#code for movie list 1.0 program:
FILENAME = "movies.txt"

def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
        file.write(movie + "\n")

def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies

def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie)
    print()

def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(movie + " was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie + " was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

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
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()



#writer() function of the CSV (Comma Separated Values) module
writer(file) #this function will create a writer object

#writerows() method of the CSV write object
writerows(rows) #this method will write the rows to the file


#a 2-dimentional list with 3 rows and 2 columns
movies = [["Monty Python and the Holy Grail", 1975],
         ["Cat on a Hot Tin Roof", 1958],
         ["On the Waterfront", 1954]]

#how to import CSV module
import csv

#how to write the list to a CSV file
with open("movies.csv", "w", "newline="") as file:
    writer = csv.writer(file) #this code will create a writer object
    writer.writerows(movies) #this code will write the list to the file

#contents of the CSV file
Monty Python and the Holy Grail,1975
Cat on a Hot Tin Roof,1958
On the Waterfront,1954


#reader() function of the csv module
reader(file) #this function will create a reader object

#How to read data from a CSV file
with open("movies.csv", newline="") as file:
reader = csv.reader(file)
for row in reader:
print(row[0] + " (" + str(row[1]) + ")")

#The console output
Monty Python and the Holy Grail (1975)
Cat on a Hot Tin Roof (1958)
On the Waterfront (1954)


#optional arugments that can be used to change CSV format
quoting=csv.QUOTE_MINIMAL #this will prevent double quotes from being added
quotechar=' " ' #this will change the double quote character
delimiter="," #this will change the delimiter

#code that changes the delimiter for the writer object
write = csv.writer(file, delimiter="\t")

#code that changes the delimiter for the reader object
reader = csv.reader(file, delimiter="\t")




#The code for the Movie List 2.0 program
import csv

# a file in the current directory
FILENAME = "movies.csv"

def write_movies(movies):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def read_movies():
    movies = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
        return movies

def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0] + " (" + movie[1] + ")")
    print()

def add_movie(movies):
    name = input("Name: ")
    year = input("Year: ")
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(name + " was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie[0] + " was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
        print("Not a valid command. Please try again.\n")
        print("Bye!")

if __name__ == "__main__":
    main()




#2 methods of the pickle module
dump(object, bfile) #this method will serialize the object, meaning it will convert it into a string
load(bfile) #this method will deserialize the string into an object, meaning it will convert it back into a Python object


#2-dimensional list of movies
movies = [["Monty Python and the Holy Grail", 1975],
         ["Cat on a Hot Tin Roof", 1958],
         ["On the Waterfront", 1954]]

#how to iport the pickle module
import pickle

#how to write an object to a binary file
with open("movies.bin", "wb") as file: #write binary
    pickle.dump(movies, file)

#how to read an object from a binary file
with open("movies.bin", "rb") as file: #read binary
    movies = pickle.load(file)
#the console output
[['Monty Python and the Holy Grail', 1975], ['Cat on a Hot Tin Roof', 1958], ['On the Waterfront', 1954]]



#the code for the two file I/O functions
import pickle

FILENAME = "movies.bin"

def write_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)

def read_movies():
    movies = []
    with open(FILENAME, "rb") as file:
        movies = pickle.load(file)
    return movies

#the code for the list_movies() function
def list_movies(movies):
    for i in range(len(movies)):
    movies = movies[i]
    print(str(i+1) + ". " + movies[0] + " (" + str(movies[1]) + ")")
    print()
