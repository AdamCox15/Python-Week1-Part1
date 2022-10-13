### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

def create_new_book():
   title = input("What is the title of the book you would like to add? ")
   author = input("Who is the author of the book you would like to add? ")
   year = input("What year was this book published? ")
   rating = input("What rating out of 5 would you give this book? ")
   pages = input("What is the page count of the book? ")
   
   book_dictionary = {
       "title": title,
       "author": author,
       "year": year,
       "rating": rating,
       "pages": pages
   }
   
   return book_dictionary

print(create_new_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def create_new_books():
   title = input("What is the title of the book you would like to add? ")
   author = input("Who is the author of the book you would like to add? ")
   year = int(input("What year was this book published? "))
   rating = float(input("What rating out of 5 would you give this book? "))
   pages = int(input("What is the page count of the book? "))
   
   book_dictionary = {
       "title": title,
       "author": author,
       "year": year,
       "rating": rating,
       "pages": pages
   }
   
   return book_dictionary




### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def create_new_book():
   title = input("What is the title of the book you would like to add? ")
   author = input("Who is the author of the book you would like to add? ")
   try: 
     year = int(input("What year was this book published? "))
   except:
    year = int(input("Please type a number for the year? "))
   try: 
    rating = float(input("What rating out of 5 would you give this book? "))
   except:
    rating = float(input("Please type a number or float number like 4.5 for the rating? "))
   try:
    pages = int(input("What is the page count pof the book? "))
   except:
    pages = int(input("Please type a number for the number of pages? "))

   
   book_dictionary = {
       "title": title,
       "author": author,
       "year": year,
       "rating": rating,
       "pages": pages
   }
#    print(type(year))
#    print(type(rating))
#    print(type(pages))
   my_books.append(book_dictionary)
   print(book_dictionary)
   home_page()


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
my_books = [
    {
        "title": "Fear and Loathing in Las Vegas",
        "author": "Hunter S Thompson",
        "year": 1997,
        "rating": 4.8,
        "pages": 345
    },
    {
        "title": "The B.F.G",
        "author": "That one Guy",
        "year": 2001,
        "rating": 4.1,
        "pages": 498
    },
    {
        "title": "Married with Children",
        "author": "Al Bundy",
        "year": 2007,
        "rating": 4.4,
        "pages": 398
    },
    {
        "title": "Edmonton Oilers",
        "author": "Connor McDavid",
        "year": 2022,
        "rating": 4.5,
        "pages": 421
    }
]

def see_books():
    for books in my_books:
        print(books)

def home_page():
    in_select = int(input("To add a book type 1. To view all the books type 2.  "))
    if in_select == 1:
        create_new_book()
    elif in_select == 2:
        see_books()
    else:
        print('please select an option from the menu')

home_page()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

my_books = [
    {
        "title": "Fear and Loathing in Las Vegas",
        "author": "Hunter S Thompson",
        "year": 1997,
        "rating": 4.8,
        "pages": 345
    },
    {
        "title": "The B.F.G",
        "author": "That one Guy",
        "year": 2001,
        "rating": 4.1,
        "pages": 498
    },
    {
        "title": "Married with Children",
        "author": "Al Bundy",
        "year": 2007,
        "rating": 4.4,
        "pages": 398
    },
    {
        "title": "Edmonton Oilers",
        "author": "Connor McDavid",
        "year": 2022,
        "rating": 4.5,
        "pages": 421
    }
]

def see_books():
    for books in my_books:
        print(books)

def home_page():
    quit = True
    while quit == True:
     in_select = int(input("To add a book type 1. To view all the books type 2. To quit type 3. "))
     if in_select == 1:
        create_new_book()
     elif in_select == 2:
        see_books()
     elif in_select == 3:
        quit = False
     else:
        print('please select an option from the menu')

home_page()
