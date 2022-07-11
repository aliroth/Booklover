from booklover import Booklover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        
        test_object = Booklover("test person","test@test.com", "drama")
        
        test_object.add_book("test book", 3)
        message = 'Book was not added to the book_list!'
        self.assertTrue(test_object.has_read("test book"), message)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        
        test_object = Booklover("test person","test@test.com", "drama")
        
        test_object.add_book("test book", 3)
        test_object.add_book("test book", 3)
        test = len([x for x in list(test_object.book_list["book_name"].values) if x == "test book"]) == 1
        message = 'Book was incorrectly added to the book_list!'
        self.assertTrue(test, message)
        
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        
        test_object = Booklover("test person","test@test.com", "drama")
        
        test_object.add_book("test book", 3)
        message = "The .has_read() method does not recognize the book"
        self.assertTrue(test_object.has_read("test book"), message)
        
    def test_4_has_read(self):
         # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
        test_object = Booklover("test person","test@test.com", "drama")
        
        test_object.add_book("test book", 3)
        message = "The .has_read() method incorrectly recognized the book"
        self.assertFalse(test_object.has_read("testing book"), message)
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        
        test_object = Booklover("test person","test@test.com", "drama")
        
        testVal = 3
        test_object.add_book("test book1", 1)
        test_object.add_book("test book2", 2)
        test_object.add_book("test book3", 3)
        fnum = test_object.num_books_read()
        message = 'Books were not added to the book_list!'
        self.assertEqual(testVal, fnum, message)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        test_object = Booklover("test person","test@test.com", "drama")
        
        test_object.add_book("test book1", 1)
        test_object.add_book("test book2", 2)
        test_object.add_book("test book4", 4)
        testList = test_object.fav_books()
        test = (x > 3 for x in testList["book_rating"])
        message = "fav_books was not generated correctly"
        self.assertTrue(test, message)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)