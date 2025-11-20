class publisher:
    def __init__(self, name):
        print("publisher class activated")
        self.name = name

    def display(self):
        print(f"name: {self.name}")

class book(publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        print("book class activated")
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print(f"title: {self.title}")
        print(f"author: {self.author}")

class python(book):
    def __init__(self, name, title, author, price, no_pages):
        super().__init__(name, title, author)
        print("python class activated")
        self.price = price
        self.no_pages = no_pages

    def display(self):
        super().display()
        print(f"price: {self.price}")
        print(f"no of pages: {self.no_pages}")
book1=python("dc","aadujeevitham","asheer",540,350)
book1.display()