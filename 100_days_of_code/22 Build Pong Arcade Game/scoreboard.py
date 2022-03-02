from turtle import Turtle


class Scoreboard(Turtle):
    """ scoreboard class """

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """ write the :l_score: and :r_score: at the top of the screen """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 40, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 40, 'bold'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


#tags: __init__()
