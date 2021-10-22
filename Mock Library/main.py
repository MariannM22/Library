from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title:str
    author:str
    borrower_name:str

def add_books(book_log: List[Book])->None:
    print("Title?")
    title = input("> ")
    print("Author(s)?")
    author = input("> ")
    book_log.append(Book(title,author,""))

def view_books(book_log: List[Book])->None:
    i = 0
    for book in book_log:
        i += 1
        if len(book.borrower_name) == 0:
            availability = "Available"
        else:
            availability = "Unavailable"
        print(f"{i}. [{availability}] {book.title} by {book.author}")


def loan_books(book_log: List[Book])->None:
    print("Which book?")
    i = 0
    for book in book_log:
        i += 1
        if len(book.borrower_name) == 0:
            print(f"{i}. {book.title} by {book.author}")
    which_book = int(input("> "))
    book = book_log[which_book -1]
    print("Borrower's name?")
    borrower = input("> ")
    book.borrower_name = borrower



def return_books(book_log: List[Book])->None:
        print("Title?")
        title = input("> ")
        for book in book_log:
            if book.title == title:
                print("Borrower's name?")
                borrower = input("> ")
                if book.borrower_name == borrower:
                    book.borrower_name = ""


def main()-> None:
    book_log = []
    while True:
        print("add [book], [view] inventory, [loan] book, [return] book, [quit]?")
        choice = input("> ")
        if choice == "book":
            add_books(book_log)
        if choice == "view":
            view_books(book_log)
        if choice == "loan":
            loan_books(book_log)
        if choice == "return":
            return_books(book_log)
        if choice == "quit":
            break
if __name__ == '__main__':
    main()
