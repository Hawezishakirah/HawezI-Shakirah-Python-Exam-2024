# í)
class Book:
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def my_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


my_book = Book("The curse of the sacred cow", "Hawezi Shakirah", 300)
my_book.my_book()



# íí)
class Book:
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def my_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class EBook(Book):
    
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format  
    

    def my_book(self):
        super().my_book()   
        print(f"Format: {self.format}")

new_book = EBook("The curse of the sacred cow", "Hawezi Shakirah", 300, "quin")
new_book.my_book()



# ííí)
class Book:
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
    

    def title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"

my_book = Book("The curse of the sacred cow", "Hawezi Shakirah",300)
print(my_book.title_and_author())


# v)
#a)class is a 