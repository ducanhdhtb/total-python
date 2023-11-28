# Encapsulation:
# Encapsulation involves hiding the internal state of an object, allowing access only through defined methods or properties.

# Đóng Gói (Encapsulation):
# Đóng gói liên quan đến việc ẩn trạng thái nội tại của một đối tượng, chỉ cho phép truy cập thông qua các phương thức hoặc thuộc tính được xác định.

class Person:
    public_attribute = "Show" # Accessiable from the outside
    __private_attribute = "Hidden" # Not accessiable

    # Not accessiable from the outside
    def __hidden_method(self):
        print("This method is hidden")
        self.__private_attribute = 0

    # Accessiable from the outside
    def normal_method(self):
        # This method is accessiable from the inside
        self.__hidden_method()

student = Person()
# student.__hidden_method() # this method is not accessible from outside
# student.normal_method()
