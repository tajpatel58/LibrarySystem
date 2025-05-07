class Book:
    def __init__(self, title: str, author: str, page_count: int, isbn: int, in_stock: bool = 'True'):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.in_stock = in_stock