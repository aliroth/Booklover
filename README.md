# Booklover

Booklover class creates a dataframe to track books read and ratings.

# Installation
pip install Booklover 

## Usage
from Booklover import Books \
from Books import booklover 

# Parameters
 Booklover(name, email, genre, num_books = 0) \
-  name (string) : person's name \
-  email (string) : person's email \
-  genre (string) : favorite book genre \
-  num_books (int) : defualts to 0 

# Methods
add_book(book, rating) \
-  adds a book and cooresponding rating to the dataframe \
has_read(book) \
-  tests to see if the book passed is already in the dataframe \
num_books_read() \
-  returns the number of books in the dataframe \
fav_books() \
-  returns the books from the dataframe with a rating greater than 3
