from turtle import Turtle

class Answer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def make_answer(self, x, y, state):
        self.goto(x, y)
        self.write(f'{state}', align='center', font=('Arial', 8, 'normal'))
