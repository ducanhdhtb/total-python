class Wizard():
    def defend(self):
        print("magic shield")
class Archer():
    def defend(self):
        print("duck")
class Samurai():
    def defend(self):
        print("block")
def general_defense(character):
    character.defend()


#
# Trong đoạn mã trên, tính chất đa hình được thể hiện qua việc sử dụng hàm `general_defense`
# để thực hiện hành động phòng thủ trên các đối tượng thuộc các lớp khác nhau (`Wizard`, `Archer`, `Samurai`).
# Mặc dù các lớp này có phương thức `defend` khác nhau, nhưng hàm `general_defense` có thể hoạt động chung trên tất cả chúng.
#
# Cụ thể:
#
# 1. Lớp `Wizard` có phương thức `defend` in ra thông báo "magic shield".
# 2. Lớp `Archer` có phương thức `defend` in ra thông báo "duck".
# 3. Lớp `Samurai` có phương thức `defend` in ra thông báo "block".
#
# Hàm `general_defense` nhận một đối tượng làm đối số và gọi phương thức `defend` trên đối tượng đó. Bất kỳ đối tượng thuộc các lớp nào cũng có thể được truyền vào hàm này mà không cần biết chi tiết về kiểu cụ thể.
#
# Ví dụ:
#
# ```python
# gandalf = Wizard()
# hawkeye = Archer()
# jack = Samurai()
#
# general_defense(gandalf)  # In ra: "magic shield"
# general_defense(hawkeye)  # In ra: "duck"
# general_defense(jack)     # In ra: "block"
# ```
#
# Tính chất đa hình ở đây cho phép cùng một hàm (`general_defense`) hoạt động trên nhiều loại đối tượng khác nhau mà không cần biết chi tiết về từng loại cụ thể.