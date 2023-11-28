class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'"{self.title}", from {self.author}'


# Tạo một đối tượng Book
my_book = Book("The Python Book", "John Doe", 300)

# Gọi hàm str() trên đối tượng Book
book_str = str(my_book)

# In chuỗi mô tả đối tượng Book
print(book_str)  # Output: "The Python Book", from John Doe
