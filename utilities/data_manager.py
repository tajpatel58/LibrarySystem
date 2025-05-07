def name_and_information_for_book(book_contents: dict):    
    for book_name, details in book_contents.items():
        print(f"Book: {book_name}")
        print(f"Author: {details['author']}")
        print(f"Page Count: {details['page_count']}")
        print(f"Year Released: {details['year_of_release']}")

from datetime import datetime

def get_overdue_dates(date_list: list[str]) -> list[str]:
    date_today = datetime.today().date()
    overdue_dates = []

    for input_date in date_list:
        converted_date = datetime.strptime(input_date, "%d/%m/%Y").date()
        if converted_date < date_today:
            overdue_dates.append(input_date)

    return overdue_dates

