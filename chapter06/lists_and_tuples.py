#! usr/bin/env python3

#syntax for creating a list:
mylist = [item1, item2, ...]

#code examples: 
temps = [48.0, 30.5, 20.2, 100.0, 42.0] # 5 float values
inventory = ["staff", "hat", "shoes"] # 3 str values
movie = ["The Holy Grail", 1975, 9.99] # str, int, float
test_scores = [] # an empty list


#how to use repetition operator(*) to create a list:
scores = [1, 2, 3] * 3 #scores = [1, 2, 3, 1, 2, 3, 1, 2, 3]


#temps list:
temps = [48.0, 30.5, 20.2, 100.0, 42.0]

#its positive and negative index values
temps[0], temps[-5] # returns 48.0
temps[1], temps[-4] # returns 30.5
temps[2], temps[-3] # returns 20.2
temps[3], temps[-2] # returns 100.0
temps[4], temps[-1] # returns 42.0


#how to get an iterm in a list:

#Code that gets items from the temps list
temps = [48.0, 30.5, 20.2, 100.0, 42.0]
temp = temps[0] # temp = 48.0
temp = temps[4] # temp = 42.0
temp = temps[5] # IndexError: index out of range

#Code that gets items from the inventory list
inventory = ["staff", "hat", "shoes", "bread", "potion", "scroll"]
item = inventory[5] # item = "scroll "
item = inventory[3] # item = "bread"
item = inventory[6] # IndexError: index out of range

#How to set an item in a list
temps[3] = 98.0 # replaces 100.0 with 98.0
inventory[4] = "ration" # replaces "potion" with "ration"


#list methods for modifying a list:
append(item) # adds item to the end of the list
insert(index, item) # inserts item at index
remove(item) # removes the first occurrence of item
index(item) # returns the index of the first occurrence of item
pop([item]) # removes and returns the item at index

#append(), insert(), and remove() method examples: 
stats = [48.0, 30.5, 20.2, 100.0]

inventory = ["staff", "hat", "shoes", "bread", "potion"]

stats.append(99.5) # [48.0, 30.5, 20.2, 100.0, 99.5]

inventory.insert(3, "robe") # ["staff", "hat", "shoes", # "robe", "bread", "potion"]

inventory.remove("shoes") # ["staff", "hat", "robe", # "bread", "potion"]

#the pop() method:
inventory = ["staff", "hat", "robe", "bread"]
item = inventory.pop() # item = "bread" and inventory = ["staff", "hat", "robe"]
item = inventory.pop(1) # item = "hat" and inventory = ["staff", "robe"]

#the index() and pop() methods: 
inventory = ["staff", "hat", "robe", "bread"]
i = inventory.index("hat") # 1
inventory.pop[i] # ["staff", "robe", "bread"]


#a built in function for getting the length of a list:
len(list)


#how to use the in keyword to check whether an iterm is in a list:
inventory = ["staff", "hat", "bread", "potion"]
item = "bread"
if item in inventory:
    inventory.remove(item) # ["staff", "hat", "potion"]


#how to print list to the console:
inventory = ["staff", "hat", "shoes", "bread", "potion"]
print(inventory) #prints: ["staff", "hat", "shoes", "bread", "potion"]


#the syntax for looping through a list:
for item in list:
    statements

#code that prints each item in a list:
inventory = ["staff", "hate", "shoes"]
for item in inventory:
    print(item)


#How to process the items in a list
#With a for loop
scores = [70, 80, 90, 100]
total = 0
for score in scores:
    total += score
print(total) # 340

#With a while loop
scores = [70, 80, 90, 100]
total = 0
i = 0
while i < len(scores):
    total += scores[i]
    i += 1
print(total) # 340


#four immunatable types:
str
int
float
bool

#one mutable type:
list


#How to work with immutable arguments:
#The double_the_number() function
def double_the_number(value):
value = value * 2 # new int object created
return value # new int object must be returned

#The calling code in the main() function
value1 = 25 # int object created
value2 = double_the_number(value1)
print(value1) # 25
print(value2) # 50


#how to work with mutable arguments:
#The add_to_list() function
def add_to_list(list, item):
list.append(item) # list object changed

#The calling code in the main() function
inventory = ["staff", "hat", "bread"] # list object created
add_to_list(inventory, "robe")
print(inventory) # ["staff", "hat", "bread", "robe"]
# Note: no need to return list object



#The code for the Movie List program:
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def list(movie_list):
    i = 1
    for movie in movie_list:
        print(str(i) + ". " + movie)
        i += 1
    print()

def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(movie + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie + " was deleted.\n")

def main():
    movie_list = ["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
main()



#How to define a list of lists...
#ith 3 rows and 4 columns
students = [["Joel", 85, 95, 70],
            ["Anne", 95, 100, 100],
            ["Mike", 77, 70, 80, 85]]

#With 3 rows and 3 columns
movies = [["The Holy Grail", 1975, 9.99],
          ["Life of Brian", 1979, 12.30],
          ["The Meaning of Life", 1983, 7.50]]


#how to add to a list of lists through programming:
movies = [["The Holy Grail", 1975, 9.99],
["Life of Brian", 1979, 12.30]]

movie = [] # Create empty movie
movie.append("The Meaning of Life") # Add name to movie
movie.append(1983) # Add year to movie
movie.append(7.5) # Add price to movie
movies.append(movie) # Add movie to movies


#how to access the iterms in the list of movies:
movies[0][0] # "The Holy Grail"
movies[0][2] # 9.99
movies[0][3] # IndexError: index out of range
movies[1][0] # "Life of Brian"
movies[3][0] # IndexError: index out of range


#how to print two-dimentional list:
print(movies)
# [['The Holy Grail', 1975, 9.99], ['Life of Brian', 1979, 12.30], ['The Meaning of Life', 1983, 7.5]] 


#how to loop through the rows and colums of a two-dimentional list:
for movie in movies:
    for item in movie:
        print(item, end=" | ")
    print()



#The code for the Movie List 2D program:
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
        i += 1
    print()
    
def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = []
    movie.append(name)
    movie.append(year)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def main():
    movie_list = [["Monty Python and the Holy Grail", 1975], 
                 ["On the Waterfront", 1954],   
                 ["Cat on a Hot Tin Roof", 1958]]

    display_menu()

    while True:
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
main()



#more list methods:
count(item) # returns the number of times item appears in the list
reverse(item) # reverses the order of the list
sort([key=function]) # sorts the list, key is a function

#a built in function:
sorted(list[, key=function])

#count(), reverse(), and sort() method:
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]

count = numlist.count(14) # 2
numlist.reverse() # [25, 14, 10, 8, 2, 14, 3, 84, 15, 5]
numlist.sort() # [2, 3, 5, 8, 10, 14, 14, 15, 25, 84]


#The sort() method with mixed-case lists:
foodlist = ["orange", "apple", "Pear", "banana"]

#What happens in a simple sort
foodlist.sort() # ["Pear", "apple", "banana", "orange"]

#How to use the key argument to fix the sort order
foodlist.sort(key=str.lower) # ["apple", "banana", "orange", "Pear"]


#two more built-in functions:
min(list) # returns the smallest item in the list
max(list) # returns the largest item in the list

#two functions of the random module:
choice(list) # returns a random item from the list
shuffle(list) # shuffles the items in the list 

#How to use the min() and max() functions
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
minimum = min(numlist) # 2
maximum = max(numlist) # 84

#How to use the choice() and shuffle() functions
import random
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14]
choice = random.choice(numlist) # gets random item
random.shuffle(numlist) # shuffles items randomly


#the deepcopy() function:
deepcopy(list)

#how to make a shallow copy of a list:
list_one = [1, 2, 3, 4, 5]
list_two = list_one
list_two[1] = 4
print(list_one) # [1, 4, 3, 4, 5]
print(list_two) # [1, 4, 3, 4, 5]

#How to make a deep copy of a list
import copy
list_one = [1, 2, 3, 4, 5]
list_two = copy.deepcopy(list_one)
list_two[1] = 4
print(list_one) # [1, 2, 3, 4, 5]
print(list_two) # [1, 4, 3, 4, 5]


#how to slice a list:
#the syntax for slicing a list
mylist[start:end:step] #end is exclusive

#code that slices with the start and end arguments
numbers = [52, 54, 56, 58, 60, 62]
numbers[0:2] # [52, 54]
numbers[:2] # [52, 54] #if start is not specified, it defaults to 0
numbers[4:] # [60, 62] #if end is not specified, it defaults to the length of the list

#Code that slices with the step argument
numbers[0:4:2] # [52, 56]
numbers[::-1] # [62, 60, 58, 56, 54, 52] #if start and end are not specified, they default to 0 and the length of the list


#How to concatenate two lists with the + and += operators
inventory = ["staff", "robe"]
chest = ["scroll", "pestle"]

combined = inventory + chest
# ["staff", "robe", "scroll", "pestle"]

print(inventory)
# ["staff", "robe"]

inventory += chest
# ["staff", "robe", "scroll", "pestle"]

print(inventory)
# ["staff", "robe", "scroll", "pestle"]


#how to create a tuple:
mytuple = (item1, item2, ...)

#code that creates tuple:s:
# a tuple of 5 floating-point numbers
stats = (48.0, 30.5, 20.2, 100.0, 48.0)

# a tuple of 6 strings
herbs = ("lavender", "pokeroot", "chamomile",
"valerian", "nettles", "oatstraw")

# a tuple that stores the data for a movie
movie = ("Monty Python and the Holy Grail", 1975, 9.99)


#code that accesses items in a tuple:
herbs[0] # lavender
herbs[-1] # oatstraw
herbs[1:4] # ('pokeroot', 'chamomile', 'valerian')

herbs[1] = "red clover"
# TypeError: 'tuple' object does not support
# item assignment


#code that unpacks a tuple:
tuple_values = (1, 2, 3)
a, b, c = tuple_values # a = 1, b = 2, c = 3


#function that returns a tuple:
def get_location():
    #code that computes values for x, y, and z
    return x, y, zip

#code that calls the get_location() function and unpacks the returned tuple
x, y, z = get_location()



#the number cruncher program:
import random

def crunch_numbers(data):
    total = 0
    for number in data:
        total += number

    average = round(total / len(data))
    median_index = len(data) // 2
    median = data[median_index]
    minimum = min(data)
    maximum = max(data)
    dups = get_duplicates(data)

    print("Average =", average,
    "Median =", median,
    "Min =", minimum,
    "Max =", maximum,
    "Dups =", dups)

def get_duplicates(data):
    dups = []
    for i in range(51):
        count = data.count(i)
        if count >= 2:
            dups.append(i)
    return dups
def main():
    fixed_tuple = (0,5,10,15,20,25,30,35,40,45,50)
    random_list = [0] * 11
    for i in range(len(random_list)):
        random_list[i] = random.randint(0, 50)
    random_list.sort()

    print("TUPLE DATA:", fixed_tuple)
    crunch_numbers(fixed_tuple)
    print()
    print("RANDOM DATA:", random_list)
    crunch_numbers(random_list)

# if started as the main module, call the main() function
if __name__ == "__main__":
main()
