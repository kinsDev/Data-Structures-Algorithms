class Book:
    def __init__(self, ID, title):
        self.ID = ID
        self.__title = title


harry_potter = Book(3789, 'Harry Potter and the Chamber of Secrets')
print(harry_potter._Book__title)
