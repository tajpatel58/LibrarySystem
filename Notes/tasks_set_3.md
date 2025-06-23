
# 📚 Library System Project - Beginner Python Tasks

Welcome to the Library System project! This is a hands-on Python learning experience that will help you get comfortable with real-world coding concepts such as working with files, object-oriented programming, and managing dependencies.

---

## ✅ Task 1: Learn About JSON Data Format + Write a function to read in a JSON file:

**Goal**: Understand what JSON is and how to interact with JSON files in Python.

### 🔍 Description:
- JSON (JavaScript Object Notation) is a common data format used to store structured data.
- You will need to read a JSON file which contains the book information and convert it into a Python dictionary.
- You’ll then access and create Books objects for each book we have in our dictionary. 
- Write a function to read in a JSON file, and try read in books.json in the data folder. Also practice accessing values within this dictionary. 
- Are you able to create a book object for each book we have in our json data? 

---

## ✅ Task 2: Create a `requirements.txt` with UV

**Goal**: Understand and manage project dependencies using a `requirements.txt` file.

### 🔍 Description:
- Learn what `requirements.txt` is and why it's used.
- Use [uv](https://github.com/astral-sh/uv) to create a virtual environment and export your dependencies.

---

## ✅ Task 3: Add a `balance_owed` Method in the `User` Class + Static Methods

**Goal**: Implement a pricing strategy for overdue books.

### 🔍 Description:
- Create a "classes.md" file in "notes" folder. In "classes.md" write a paragraph on what a static method is. 
- Create a rule system (up to you) that calculates how much a user owes based on how long a book is overdue.
- The task here is to write a "static method" within the User Class calculates that takes in 1 input as a date, and based on the number of days the book is overdue a penalty is calculated. 

### 💡 Example Logic to Use:
- £1 for **each day** overdue.
- An **extra £10** penalty for **every full month** (30 days) it is overdue.

---

## ✅ Task 4: Add New Attributes to the `User` Class

**Goal**: Enhance the `User` class to track borrowed books and account balance.

### 🔍 Description:
- Note: Adding attributes should be done in the `__init__` method of a class.
- Add an attribute `borrowed_books` as an empty list to store the types of books a user has borrowed.
- Add an attribute `balance` that starts at 0.
Happy coding! 🐍
