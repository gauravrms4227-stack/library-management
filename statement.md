# Project Statement

## Problem Statement
Small libraries, classrooms, or personal book collections are often
managed manually — through notebooks or memory — making it hard to
keep track of which books are available and which have been borrowed.
This can lead to lost books, confusion over who has what, and no
simple way to view the collection at a glance. There is a need for a
lightweight tool that lets someone quickly record books, track their
borrow/return status, and manage the collection without relying on
complex software.

## Scope of the Project
Library Book Manager is a command-line application that allows a
single user to:
- Add books to a library collection
- View all books along with their current status
- Borrow and return books
- Remove books from the collection

The scope is limited to single-user, local (offline) use, with data
stored in a simple text file. It does not include multi-user access,
member/user accounts, due-date tracking, or online/cloud syncing.

## Target Users
- Students or individuals managing a small personal book collection
- Classroom teachers keeping track of a shared set of books
- Small community or home libraries that don't need full library
  management software
- Beginners learning Python who want to see a simple, real-world
  example of file handling and CRUD-style operations

## High-Level Features
1. **Add Book** — Record a new book with its title and author; it
   starts out marked as "Available."
2. **View Books** — See a numbered list of every book in the library
   along with its current status (Available or Borrowed).
3. **Borrow Book** — Mark an available book as borrowed.
4. **Return Book** — Mark a borrowed book as available again.
5. **Remove Book** — Delete a book from the library collection.
6. **Persistent Storage** — All changes are automatically saved to a
   text file so the library is remembered the next time the program
   runs.