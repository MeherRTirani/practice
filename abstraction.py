from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=3.14*self.radius**2
        print("Area of circle is",a)

    def perimeter(self):
        b = 2*3.14*self.radius
        print("Perimeter of circle is", b)

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        b= self.side**2
        print("Area of square is",b)

    def perimeter(self):
        c=self.side*4
        print("Perimeter of square is",c)

circle = Circle(3)
square = Square(2)
circle.area()
circle.perimeter()
square.area()
square.perimeter()
