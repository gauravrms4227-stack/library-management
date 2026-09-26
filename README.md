# Library Book Manager

A little command-line tool I built to keep track of books in a small library — who's borrowed what, what's still on the shelf, and so on. Nothing fancy, just plain Python. No external libraries, no complicated logic, just the basics: lists, loops, functions, and a text file to remember everything.

## What it does

- Add a book to the library (title + author)
- See every book you've got, along with whether it's available or already borrowed
- Borrow a book
- Return a book
- Remove a book you no longer want on the list

## Getting it running

You just need Python 3 installed — nothing else.

1. Grab `library_book_manager.py`
2. Open a terminal in that folder
3. Run it:
   ```
   python library_book_manager.py
   ```

That's it. A menu pops up and you take it from there.

## How the data is saved

Every book gets written to a file called `books.txt`, one per line, like this:

```
title,author,status
```

You don't have to do anything for this to happen — it saves automatically every time you add, borrow, return, or remove a book. So if you close the program and come back later, your books are still there.

## The menu

```
1. Add book
2. View books
3. Borrow book
4. Return book
5. Remove book
6. Exit
```

## What it looks like

```
1. The Alchemist by Paulo Coelho - Available
2. Atomic Habits by James Clear - Borrowed
```

## Ideas for later

If I ever come back to this, a few things worth adding:
- Searching by title or author instead of scrolling the whole list
- Due dates for borrowed books
- Handling multiple copies of the same book

## Why it's built this way

This was kept intentionally simple — no classes, no imports beyond basic file handling, nothing you wouldn't already know a month into learning Python. It's meant to be easy to read top to bottom and understand exactly what every line is doing.