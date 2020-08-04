# -*- coding: utf-8 -*-
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.days = []

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    # assume name is unique
    def issueBook(self, name, days=10):
        if name in self.name:
            if days == self.days:
                return self.name + ' ' + self.days

    # assume name is unique
    def returnBook(self, name):
        if name in self.name:
            if name == self.name:
                return self.name


class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        self.publish_date = []
        self.pages =[]

    def __repr__(self):
        return self.name + self.location + self.emp_id

    def addBook(self):
        Library.books.append(self.name, self.author, self.publish_date, self.pages)

    def removeBook(self, name):
        if name == self.name:
            Library.books.remove(self.name)

    def removeBookItemFromCatalog(self, catalog, book, isbn):
        Library.remove(catalog)
        Library.remove(book)
        Library.remove(isbn)