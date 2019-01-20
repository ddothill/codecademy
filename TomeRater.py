class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
# dictionary for books and their rating
        self.books = {}

    def get_email(self, name):
        return self.email

    def change_email(self, address):
        self.email = self.address
        print("This user's email address has been updated.")

    def __repr__(self):
        return "User {user}, email: {email}, books read: {book_count}".format(user=self.name, email=self.email, book_count=self.books)

    def __eq__(self, other_user):
        flag = False
        if self.name == self.other_user[0] and self.email == self.other_user[1]:
            flag = True
        return flag

    def read_book(self, book, rating=None):
        self.books[self.book] = self.rating

    def get_average_rating(self):
        total_rating = 0
        books_rated = 0
        for book in self.books.values():
            total_rating += book
            if book != None:
                books_rated += 1
        return total / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if self.rating >=0 and self.rating <=4:
            self.ratings.append[self.rating]
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        flag = False
        if self.title == self.other_book[0] and self.isbn == self.other_book[1]:
            flag = True
        return flag

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return self.title + " by " + self.author

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater(object):
    def __init__(self):
# dictionary for mapping user's email to corresponding User object
        self.users = {}
# dictionary for books and how many times they have been read
        self.books = {}

    def create_book(self, title, isbn):
        self.title = title
        self.isbn = isbn
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        self.book = book
        self.email = email
        self.rating = rating
        getattr(self.users, "email", "No user with email {email}".format(email=self.email))
        self.email = User.read_book(self.book, self.rating)
        self.book = add_rating(self.rating)
        if hasattr(self.books, self.book):
            self.books[self.book] += 1
        else:
            self.books[self.book] = 1

    def add_user(self, name, email, user_books=None):
        self.name = name
        self.email = email
        self.user_books = user_books
        new_user = User(self.name, self.email)
        if user_books != None:
            for book in self.user_books:
                add_book_to_user(book, self.email)

    def print_catalog(self):
        catalog = {key:value for key, value in self.books}
        print(catalog)

    def print_users(self):
        user_dict = {key:value for key, value in self.users}
        print(user_dict)

    def most_read_book(self):
        popular_title = ""
        read_count = 0
        for book, times_read in self.books.items():
            if times_read > read_count:
                popular_title = book
        return popular_title

    def highest_rated_book(self):
        return # page 9

    def most_positive_user(self):
        return # page 9
