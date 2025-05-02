# 📚 Tasks 1 for Library System

These tasks are designed to help you learn Python by solving real-world problems in a library system.

## 📅 Task 1: Standardize Date Formats

**Problem**:  
You want to ensure that dates in your system are stored consistently. Dates can be input in one of two formats:
- `"2nd May 2025"` (long format)
- `"02/05/2025"` (short format)

Write a function that takes one of these date strings and returns a string in the format `"DD/MM/YYYY"`.

### Function Signature:
```python
def standardize_date(date_str: str) -> str:
    pass
```

### Rules:
- If the string contains `/`, assume it’s already in the correct format.
- Otherwise, convert the `"2nd May 2025"` format to `"02/05/2025"`.

### Example:
```python
standardize_date("2nd May 2025")     # "02/05/2025"
standardize_date("13/07/2024")       # "13/07/2024"
```

### Hint:
Use Python’s datetime package to learn how to format dates. 

---

---

## 🧠 Task 2: Check Overdue Return Dates

**Problem**:  
Each borrowed book has a return date. Write a function that takes in a list of return dates (as strings in the format `DD/MM/YYYY`) and returns only those that are **prior to today's date**.

This will help identify which books are **overdue**.

### Function Signature:
```python
def get_overdue_dates(date_list: list[str]) -> list[str]:
    pass
```

### Input:
- A list of date strings, e.g. `["01/01/2024", "15/08/2025"]`

### Output:
- A list of date strings that are before today’s date.

### Example:
```python
# Assume today's date is 02/05/2025
get_overdue_dates(["01/01/2024", "03/05/2025", "15/04/2025"])
# Output: ["01/01/2024", "15/04/2025"]
```

### Explanation:
Only the dates that are in the past (before today's date) are returned.

---

## 📘 Task 3: Book Model Class

**Problem**:  
You are building the core model of your library system. You have a JSON file (`books.json`) that contains book details such as title, author, and page count. Create a `Book` class to model this data.

Add a special attribute:
- `in_stock`: a boolean that defaults to `True`

📁 Save this class in `models/books.py`.

### Attributes to Include (example):
- `title`
- `author`
- `page_count`
- `isbn`
- `in_stock` (default = True)

### Example Usage:
```python
book = Book(title="1984", author="George Orwell", page_count=328, isbn="1234567890")
print(book.in_stock)  # Output: True
```

### Bonus:
Create a notebook to test your class by creating a few book objects and printing their details.

---

