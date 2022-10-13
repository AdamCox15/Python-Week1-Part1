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



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

