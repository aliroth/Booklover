import pandas as pd
import numpy as np

class Booklover:
    
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre, num_books = 0):
        self.name = str(name)
        self.email = str(email)
        self.fav_genre = str(fav_genre)
        self.num_books = int(num_books)
        
    def add_book(self, book_name, rating):
        if book_name in list(self.book_list.book_name):
            print("Book is already in your list!")
        else:          
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]})

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self, book_name):
        if book_name in list(self.book_list.book_name):
            return True
        elif book_name not in list(self.book_list.book_name):          
            return False
        
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
        