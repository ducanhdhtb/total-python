class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages   
    def __len__(self):
        return self.pages

# Tạo một đối tượng Book
my_book = Book("The Python Book", "John Doe", 300)

# Gọi hàm len() trên đối tượng Book
book_length = len(my_book)

# In kết quả
print(f"The book has {book_length} pages.")
