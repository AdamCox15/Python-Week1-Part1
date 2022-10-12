### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['Hunter S Thompson', 'Jocko Wilink', 'Gunner Andri', 'Jk Rawling', 'Mike Tyson', 'Alex Ovechkin', 'Connor McDavid', 'Kirill Kaprizov']

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append('Jesse Puljujarvi')
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

my_authors.remove('Jk Rawling')
# Example: my_authors.remove("H.G. Wells")

# I added in a place to put .pop()
my_authors.pop()

print(my_authors)

# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[4]
# Example: my_authors[2]

# Now slice the list.

my_authors[2:7]
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

my_author_tuple = ('Ray Lewis', 'Leon Drisaitl', 'Cale Makar', 'Evegeny Kuznetsov', 'Tom Wilson')
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
# print(my_author_tuple)

### Step 3 - Sets ###

# Create a set with your authors.

my_author_set = {'Ray Lewis', 'Leon Drisaitl', 'Cale Makar', 'Evegeny Kuznetsov', 'Tom Wilson'}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
# print(my_author_set)

# Add a new author to your set.

my_author_set.add('Nathan Mckinnon')
# Example: my_author_set.add("J.R.R. Tolkien")
# print(my_author_set)

# Try adding the same author again, and be sure to print your set.

my_author_set.add('Nathan Mckinnon')
# Example: my_author_set.add("J.R.R. Tolkien")

print(my_author_set)

### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:
for authors in my_authors:
    print(authors)

for authors in my_author_set:
    print(authors)

for authors in my_author_tuple:
    print(authors)

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

