class Book:
    def __init__(self, title: str, author: str, page_count: int, year_published: int, isbn: int, in_stock: bool = 'True'):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.year_published = year_published
        self.isbn = isbn
        self.in_stock = in_stock

    def __repr__(self):
        book_as_string = f'The book name is {self.title}, written by {self.author}'
        return book_as_string
    
    def __str__(self):
        second_book_as_string = f'Book: {self.title} by {self.author}'
        return second_book_as_string