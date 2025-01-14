import e_book

def main():
    book = e_book.book("The three-body problem","Liu Cixin",351)

    book.open()
    book.book_status()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.book_status()
    book.close()
    book.next_page()
    book.next_page()
    book.book_status()
if __name__ == "__main__":
    main()