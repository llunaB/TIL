from math import pi, sqrt
from abc import ABC, abstractmethod

# 다형성이란? 하나의 변수가 서로 다른 클래스의 인수들을 가리킬 수 있는 것
# 추상클래스란? 여러 클래스의 공통점을 담고 있는 상속용 클래스. 인스턴스 생성 불가. 일반클래스로 만들려면 추상메서드 오버라이딩 필수!!!
# ABC = Abstract Base Class

class Shape(ABC):
    """도형 추상 클래스"""
    @abstractmethod
    def area(self):
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩 할 것"""
        pass

    @abstractmethod
    def perimeter(self):
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩 할 것"""
        pass


class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class EqualateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    def area(self):
        """삼각형의 넓이를 리턴한다"""
        return sqrt(3) / 4 * (self.side ** 2)

    def perimeter(self):
        """삼각형의 둘레를 리턴한다"""
        return 3 * self.side

    def __str__(self):
        """삼각형의 정보를 문자열로 리턴한다"""
        return "한 변이 {}인 정삼각형".format(self.side)

class RightTriangle(Shape):
    """직각삼각형 클래스"""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """직각삼각형의 넓이를 리턴한다"""
        return self.base * self.height / 2

    def perimeter(self):
        """직각삼각형의 둘레를 리턴한다"""
        return sqrt((self.base ** 2) + (self.height ** 2)) + self.base + self.height


class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴한다"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):  #=> add_shape 메서드에 Shape 타입을 가지는 인스턴스가 파라미터로 들어와야함을 알려주는 type hinting
        """그림판에 도형을 추가한다"""
        # shape 이 Shape 클래스의 인스턴스인지 확인한다, 자식 클래스의 인스턴스 = 부모 클래스의 인스턴
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print('넓이와 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.')

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이를 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


rectangle = Rectangle(2, 2)
circle = Circle(4)
cylinder = Cylinder(3, 5)
tri = EqualateralTriangle(4)

print(tri.area())
print(tri.perimeter())

paint_program = Paint()
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)
# cyliner 는 Shape 상속 안받으므로 추가할 수 없음
paint_program.add_shape(cylinder)
# triangle 은 Shape 추상클래스를 상속받음
paint_program.add_shape(tri)

areas = paint_program.total_area_of_shapes()
perimeters = paint_program.total_perimeter_of_shapes()

print(areas)
print(perimeters)
print(paint_program)

