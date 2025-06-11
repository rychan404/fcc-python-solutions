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
        string = f'{__class__.__name__}('
        if self.width == self.height:
            string += f'side={self.width})'
        else:
            string += f'width={self.width}, height={self.height})'
        return string
        
class Square(Rectangle):
    pass

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
