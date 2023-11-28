class Wizard():
    def attack(self):
        print("magic attack")
class Archer():
    def attack(self):
        print("shoot arrow")
class Samurai():
    def attack(self):
        print("katana attack")
gandalf = Wizard()
hawkeye = Archer()
jack = Samurai()
characters = [hawkeye, gandalf, jack]
for char in characters:
    char.attack()

# Trong đoạn mã trên, đa hình được thể hiện thông qua việc sử dụng một phương thức chung có tên là `attack` trong các lớp `Wizard`, `Archer`, và `Samurai`. Mặc dù tên của phương thức giống nhau, nhưng nó được triển khai khác nhau trong mỗi lớp.
#
# Cụ thể:
#
# 1. Lớp `Wizard` có phương thức `attack` in ra thông báo "magic attack".
# 2. Lớp `Archer` có phương thức `attack` in ra thông báo "shoot arrow".
# 3. Lớp `Samurai` có phương thức `attack` in ra thông báo "katana attack".
#
# Khi bạn tạo các đối tượng `gandalf` (Wizard), `hawkeye` (Archer), và `jack` (Samurai) và đặt chúng vào một danh sách `characters`, sau đó sử dụng vòng lặp để gọi phương thức `attack` trên mỗi đối tượng trong danh sách, bạn thấy rằng mỗi đối tượng thực sự gọi đúng phương thức của lớp của nó.
#
# ```python
# # Kết quả của đoạn mã:
# # "shoot arrow"
# # "magic attack"
# # "katana attack"
# ```
#
# Điều này minh họa tính chất đa hình, vì mặc dù chúng ta gọi cùng một phương thức `attack`, nhưng hành vi của phương thức đó phụ thuộc vào loại cụ thể của đối tượng được gọi.