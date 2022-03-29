class Book:
    bookshowroom = "ABC bookshop"  # class attribute

    def __init__(self, title) -> None:  # title is Instance Attribute
        self.title = title

    def bookname(self):
        return f"Name of the book is : {self.title}"

    def __repr__(self) -> str:
        return "This class is about the books data in ABC bookshop"


b1 = Book("The Harry Porter")
print(b1)
print(b1.bookname())
print(b1.bookshowroom)
b1.bookshowroom = "AWS bookshop"
print(b1.bookshowroom)
print()
b2 = Book("The Dark Knight")
print(b2)
print(b2.bookname())
print(b2.bookshowroom)
