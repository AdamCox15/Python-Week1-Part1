my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_breakdown(book):
    book_str= f"{book['title']} was written by {book['author']} in {book['year']}. It has a rating of {book['rating']} and {book['pages']} pages."
    print(book_str)
    
book_breakdown(my_book)


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_author(book):
    author_str= f"{book['author']} wrote this book."
    print(author_str)
    
def get_title(book):
    title_str= f"{book['title']} is the title of the book."
    print(title_str)
    
def get_year(book):
    year_str= f"The book was written in {book['year']}"
    print(year_str)
    
def get_rating(book):
    rating_str= f"{book['rating']} is the rating of this book."
    print(rating_str)
    
def get_pages(book):
    pages_str= f"This book has {book['pages']} pages."
    print(pages_str)
    
get_author(my_book)    
get_title(my_book)    
get_year(my_book)    
get_rating(my_book)    
get_pages(my_book) 

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_length(book1,book2):
    if book1['pages'] < book2['pages']:
        return f"{book1['title']} has less pages."
    elif book2['pages'] < book1['pages']:
        return f"{book2['title']} has less pages."
    else:
        return "Both books have the same number of pages."
    
    
def best_rating(book1,book2):
    if book1['rating'] > book2['rating']:
        return f"{book1['title']} has the higher rating."
    elif book2['rating'] > book1['rating']:
        return f"{book2['title']} has a higher rating."
    else:
        return "Both books have the same rating."
    
def newer_book(book1,book2):
    if book1['year'] < book2['year']:
        return f"{book1['title']} is the newest book."
    elif book2['year'] > book1['year']:
        return f"{book2['title']} is the newest book."
    else:
        return "Both books were written in the same year."



