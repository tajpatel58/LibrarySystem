def name_and_information_for_book(book_contents: dict):    
    for book_name, details in book_contents.items():
        print(f"Book: {book_name}")
        print(f"Author: {details['author']}")
        print(f"Page Count: {details['page_count']}")
        print(f"Year Released: {details['year_of_release']}")

from datetime import datetime

def standardize_date(input_date: str) -> str:
    if '/' in input_date:
        return input_date

    suffixes = ['st', 'nd', 'rd', 'th']
    day, _, rest = input_date.partition(' ') # splits string between day and month/year
    for sfx in suffixes:
        if day.lower().endswith(sfx):
            day = day.removesuffix(sfx)
            break

    date_object = datetime.strptime(f"{day} {rest}", "%d %B %Y") # strp(time) converts the cleaned string into a datetime object
    return date_object.strftime("%d/%m/%Y") # strftime() turns the datetime object into a formatted string


from datetime import datetime

def get_overdue_dates(date_list: list[str]) -> list[str]:
    date_today = datetime.today().date()
    overdue_dates = []

    for input_date in date_list:
        converted_date = datetime.strptime(input_date, "%d/%m/%Y").date()
        if converted_date < date_today:
            overdue_dates.append(input_date)

    return overdue_dates

