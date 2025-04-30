def name_and_information_for_book(book_contents: dict):
    
    for book_name, details in book_contents.items():
        print(f"Book: {book_name}")
        print(f"Author: {details['author']}")
        print(f"Page Count: {details['page_count']}")
        print(f"Year Released: {details['year_of_release']}")