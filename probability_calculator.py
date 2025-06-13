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
    balls_counted = 0
    for _ in range(num_experiments):
        new_hat = copy.copy(hat)
        observed_balls = {e_color : 0 for e_color in expected_balls}
        new_hat.draw(num_balls_drawn)
        print(new_hat.contents)
        for o_color in new_hat.contents:
            for e_color in expected_balls:
                if o_color == e_color:
                    observed_balls[e_color] += 1
        successes = [o_num / expected_balls[o_color] for o_color, o_num in observed_balls.items()]
        balls_counted += min(successes)
    return balls_counted / num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.contents)
probability = experiment(hat1, {'yellow' : 2, 'blue' : 1}, 4, 2)
print(probability)