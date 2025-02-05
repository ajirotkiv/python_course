import datetime


class Book:

    def __init__(self, title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f'Book name {self.title}, author - {self.author}, published - {self.year}, status: {self.available}'

    def is_classic(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

class Library:
    def __init__(self, books):
        self.books = books

books = []

def add_book(book):
    title = input('Enter book name: ')
    author = input('Enter author: ')
    year = input('Enter when it was published: ')

    book_instance = book(title, author, year, available=True)
    books.append(book_instance)
    print('The book added successfully')

    print(books)
add_book(Book)

book_instance1 = Book('Tau, mano mamyte', 'Bradley Trevor Greive', 2005, True)
book_instance2 = Book('Kai liudesys tave aplanko...', 'Bradley Trevor Greive', 2003, True)
book_instance3 = Book('Tai kas tas gyvenimas?', 'Bradley Trevor Greive', 2003, True)

def display_books():
    for book in books:
        return books
    print(display_books())


# def borrow_book(title):
#     for book in books_kaupiklis:
#         print('Enter book name, which you want to borrow: ')
#         if book.available():
#             print(f'You successfully borrowed this book :-) {book}')
#             book.available = False










    # def filter_books(*args, **kwargs):

# print('1. To add a new book')
# print('2. To see what is in the library')
# print('3. To borrow a book')
# print('4. To return a book')
# print('5. Books filter')
# print('6. Exit')








