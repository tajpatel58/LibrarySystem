# 📚 Library System – Python Task List

## ✅ Task 1: Convert Dictionary Data to Book Objects

**File**: `data_manager.py`

**Description**:  
Write a function that accepts a dictionary, where the keys are names of books and values are information by the book, and returns a list of Books (Book types) corresponding to those books. 

**Function Signature**:
```python
def convert_to_books(book_dicts: list[dict]) -> list[Book]:
    pass
```

### 🔍 Hints:
- You'll need to loop through the list of dictionaries.

### 💡 Example:
```python
    books_as_dict = {"The Great Gatsby": {
      "ISBN": "978-0743273565",
      "Author": "F. Scott Fitzgerald",
      "Page count": 180,
      "Published Year": 1925,
      "Genre": "Classic Literature"
    }
    }

books = convert_to_books(book_dicts)
print(books[0].title)  # Output: 1984
```

---

## ✅ Task 2: Implement `__str__` Methods

**File**: Wherever your `Book` and `User` classes are defined (e.g., `models.py`)

**Description**:  
Learn about Python's `__str__` method, which controls how your object is printed using `print()` or `str()`. Then, implement it for the `Book` and `User` classes.

### 🔍 Hints:
- `__str__` should return a string.
- Keep the output clean and informative.
- For `Book`, include only `title` and `author`.
- For `User`, include only `name` and `date_of_birth`.

### 💡 Example:
```python
# Example output for Book
print(book)  # Output: Book: 1984 by George Orwell

# Example output for User
print(user)  # Output: User: Alice, DOB: 1990-05-01
```

---

## ✅ Task 3: Implement a "Return Book" Method

**File**: Inside your `Book` class

**Description**:  
Add a method called `return_book()` to the `Book` class. This method should update the `in_stock` attribute of the book to `True`.

### 🔍 Hints:
- This method should not return anything.
- Just modify the object’s `in_stock` attribute.

### 💡 Example:
```python
book = Book("1984", "George Orwell", 1949, in_stock=False)
book.return_book()
print(book.in_stock)  # Output: True
```

---

Feel free to add unit tests or a main script to experiment with your code and verify each feature works as expected. Happy coding! 🚀