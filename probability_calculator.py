import copy
import random

class Hat:
    def __init__(self, **kwargs):
        contents = []
        for color, number in kwargs.items():
            for _ in range(number):
                contents.append(color)
        print(contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass