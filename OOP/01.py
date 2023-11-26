class Bird:
    wings = True  # Class attribute

    def __init__(self, color, species):
        self.color = color  # Instance attribute
        self.species = species  # Instance attribute

    def chirp(self):
        print("Tweet!")

    def fly(self, height):
        print(f"The bird flies {height} feet high.")
        self.chirp()  # Calling instance method

    def paint_black(self):
        self.color = "black"
        print(f"Now the bird is {self.color}")

    @classmethod
    def lay_eggs(cls, number):
        print(f"The bird laid {number} eggs.")
        cls.wings = False  # Modifying class attribute

    @staticmethod
    def look():
        print("The bird looks.")

# Example usage:
tweety = Bird(color="yellow", species="Canary")

tweety.fly(164)  # Instance method
tweety.paint_black()  # Instance method

Bird.lay_eggs(3)  # Class method
print(f"Do wings exist? {Bird.wings}")  # Accessing class attribute

Bird.look()  # Static method
#
# Trong ví dụ này:
#
# fly là một phương thức thể hiện, vì nó có thể truy cập và sửa đổi thuộc tính thể hiện (self.color) và gọi một phương thức khác của thể hiện (self.chirp()).
#
# lay_eggs là một phương thức của lớp, vì nó được đánh dấu bằng @classmethod và có tham số là cls thay vì self. Nó có thể truy cập và sửa đổi thuộc tính của lớp (cls.wings).
#
# look là một phương thức tĩnh, vì nó được đánh dấu bằng @staticmethod và không có tham số self hoặc cls. Nó không thể truy cập thuộc tính của lớp hoặc thể hiện.
#
# Khi bạn chạy mã này, bạn sẽ thấy các loại phương thức được sử dụng và cách chúng tương tác với thuộc tính của lớp và thể hiện.






