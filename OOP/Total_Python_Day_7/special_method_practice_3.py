class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __del__(self):
        print(f'Book deleted')


# Tạo một đối tượng Book
my_book = Book("The Python Book", "John Doe", 300)

# Xóa đối tượng sử dụng hàm del
#del my_book  # Khi xóa, phương thức __del__ được gọi và in ra "Book deleted"
print(my_book)