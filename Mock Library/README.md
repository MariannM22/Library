# Library

The library should manage a collection of books. The user should be able to add a new book to the library, view the books in the library, lend a book, and return a book. The program keeps track of each book's title, author(s), and who is borrowing it (if anyone is borrowing it).

Example:

```
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> book
Title?
> Series of Unfortunate Events
Author(s)?
> Lemony Snickett
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> book
Title?
> The Hate U Give
Author(s)?
> Angie Thomas
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> view
1. [Available] Series of Unfortunate Events by Lemony Snickett
2. [Available] The Hate U Give by Angie Thomas
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> loan
Which book?
1. Series of Unfortunate Events by Lemony Snickett
2. The Hate U Give by Angie Thomas
> 2
Borrower's name?
> Mariann
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> view
1. [Available] Series of Unfortunate Events by Lemony Snickett
2. [Unavailable] The Hate U Give by Angie Thomas
> loan
Which book?
1. Series of Unfortunate Events by Lemony Snickett
> 1
Borrower's name?
> Mikala
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> return
Title?
> The Hate U Give
Borrower's Name?
> Mariann
> view
1. [Unavailable] Series of Unfortunate Events by Lemony Snickett
2. [Available] The Hate U Give by Angie Thomas
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> quit
```


