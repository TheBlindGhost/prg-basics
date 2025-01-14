

class book:
    def __init__(self,title='none',author='none',num_pages=0):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.page = 1
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def next_page(self):
        if self.is_open == True:
            self.page += 1
        else:
            print("Book not open!!!!")
    def prev_page(self):
        if self.is_open == True:
            self.page -= 1
        else:
            print("Book not open!!!!")
    def book_status(self):
        if self.is_open == False:
            print(f"Book {self.title} written by {self.author} containing {self.num_pages} pages is currently closed")
        else:
            print(f"Book {self.title} written by {self.author} containing {self.num_pages} pages is currently opened on page {self.page}")
    