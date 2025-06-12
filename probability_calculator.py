import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for _ in range(number):
                self.contents.append(color)
    
    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        for _ in range(number):
            self.contents.pop(random.randint(0, len(self.contents) - 1))
        return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.draw(3))