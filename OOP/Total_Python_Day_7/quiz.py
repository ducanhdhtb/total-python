class MyClass:
    class_variable = "I am a class variable"
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        print("This is a static method")

    def instance_method(self):
        print("This is an instance method")


# Sử dụng static method
MyClass.static_method()

# Tạo một thể hiện của lớp
obj = MyClass("I am an instance variable")

# Gọi instance method qua thể hiện
obj.instance_method()

# Truy cập class variable thông qua class
print(MyClass.class_variable)
