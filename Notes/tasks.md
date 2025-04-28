# 📚 Library System

This project is a simple Library Management System that:

- Ingests **Users** from a CSV file
- Ingests **Books** from a JSON file
- Supports **borrowing** and **returning** books
- Tracks **loan dates** and **pending balances** (e.g., overdue fines)

---

## 📥 1. Reading Input Data

- Create a utility function to **read users** from a CSV file:
  - Parse each row into a `User` instance
  - Validate and handle missing/invalid data

- Create a utility function to **read books** from a JSON file:
  - Parse each object into a `Book` instance
  - Validate necessary fields like `title`, `author`, etc.

---

## 📚 2. Define Models

### `User` Class
- **Attributes**:
  - `user_id`
  - `name`
  - `email`
  - `pending_balance`
  - `borrowed_books` (list of `Book` instances)

- **Methods**:
  - `borrow_book(book, loan_date)`
  - `return_book(book, return_date)`
  - `calculate_pending_balance(current_date)` (e.g., overdue fines)
  - `show_borrowed_books()`

---

### `Book` Class
- **Attributes**:
  - `book_id`
  - `title`
  - `author`
  - `is_loaned`
  - `borrower` (reference to a `User` instance, or `None`)
  - `loan_date`

- **Methods**:
  - `loan_to(user, loan_date)`
  - `return_from_user(return_date)`

---

## 🔄 3. Core Interactions

### `LibrarySystem` Class
- **Attributes**:
  - `users` (list of `User` instances)
  - `books` (list of `Book` instances)

- **Methods**:
  - `find_user_by_id(user_id)`
  - `find_book_by_id(book_id)`
  - `loan_book_to_user(user_id, book_id, loan_date)`
  - `return_book_from_user(user_id, book_id, return_date)`
  - `list_all_loans()`
  - `list_all_pending_balances()`
  - `get_overdue_books(current_date)`

---

### 📋 Loan Policies
- Maximum loan duration: **14 days** (configurable)
- Overdue fines: **$1 per day** past due date

### 🚨 Edge Cases to Handle
- Loaning a book that is already loaned out
- Returning a book that is not currently borrowed
- (Optional) Users reaching maximum borrowing limits
