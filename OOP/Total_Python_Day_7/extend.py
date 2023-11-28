### 1. Kế Thừa Đơn (Single Inheritance):
# Trong kế thừa đơn, một lớp con có thể kế thừa từ một lớp cha duy nhất.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Sử dụng kế thừa đơn
dog = Dog()
dog.speak()  # Kế thừa từ Animal
dog.bark()   # Phương thức riêng của Dog

# Lớp `Dog` kế thừa từ lớp `Animal`,
# vì vậy nó có thể sử dụng tất cả các phương thức của lớp `Animal`,
# cũng như thêm các phương thức riêng của mình như `bark`.

### 2. Kế Thừa Đa (Multiple Inheritance):
# Trong kế thừa đa, một lớp con có thể kế thừa từ nhiều lớp cha.
class Bird:
    def fly(self):
        print("Bird can fly")

class Horse:
    def gallop(self):
        print("Horse can gallop")

class Pegasus(Bird, Horse):
    pass

# Sử dụng kế thừa đa
pegasus = Pegasus()
pegasus.fly()     # Kế thừa từ Bird
pegasus.gallop()  # Kế thừa từ Horse
```

# Lớp `Pegasus` kế thừa từ cả `Bird` và `Horse`, nó có thể sử dụng tất cả các phương thức từ cả hai lớp cha.

### 3. Kế Thừa Đa Hình (Multilevel Inheritance):

# Kế thừa đa hình xảy ra khi một lớp con được tạo ra từ một lớp con khác.


class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class ColoredCircle(Circle):
    def color(self):
        print("Adding color to the circle")

# Sử dụng kế thừa đa hình
colored_circle = ColoredCircle()
colored_circle.draw()  # Kế thừa từ Circle
colored_circle.color() # Phương thức riêng của ColoredCircle


# Lớp `ColoredCircle` kế thừa từ `Circle`, và `Circle` kế thừa từ `Shape`. Lớp `ColoredCircle` có thể sử dụng cả hai phương thức từ `Circle` và `Shape`, tạo ra một chuỗi kế thừa đa hình.