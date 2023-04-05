book_title = input()
book_from_shelf = input()

checked_books = 0
while book_title != book_from_shelf:
    if book_from_shelf == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    checked_books += 1
    book_from_shelf = input()
else:
    print(f"You checked {checked_books} books and found it.")
