class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for row in range(self.height):
            for col in range(self.width):
                picture += '*'
            picture += '\n'
        return picture

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def get_amount_inside(self, inner_shape):
        shape_width = getattr(self, 'width')
        shape_height = getattr(self, 'height')
        amount = 0
        while (shape_height >= getattr(inner_shape, 'height')):
            while (shape_width >= getattr(inner_shape, 'width')):
                shape_width -= getattr(inner_shape, 'width')
                amount += 1
            shape_height -= getattr(inner_shape, 'height')
            shape_width = getattr(self, 'width')
        return amount

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def set_height(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def __str__(self):
        return f'Square(side={self.width})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))