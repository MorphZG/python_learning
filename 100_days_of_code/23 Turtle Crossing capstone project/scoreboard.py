from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)


class Scoreboard(Turtle):

    def __init__(self):
        """ initialise score as a text on screen """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.current_score = 0
        self.text = f'current score: {self.current_score}'
        self.write(self.text, align='left', font=FONT)

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.text = f'current score: {self.current_score}'
        self.write(self.text, align='left', font=FONT)

    def gameover(self):
        """ resets the score and prints gameover """
        self.clear()
        self.goto(0, 0)
        self.text = f'GAME OVER!\nHigh score: {self.current_score}'
        self.write(self.text, align='center', font=FONT)
