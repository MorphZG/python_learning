from turtle import Turtle


FONT_STYLE = ('Courier', 15, 'bold')


class Scoreboard(Turtle):
    ''' defines Scoreboard from Turtle '''

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write(f'score: {self.current_score}', align='center', font=(FONT_STYLE))

    def update_score(self):
        ''' increase the score by 1 '''
        self.clear()
        self.current_score += 1
        self.write(f'score: {self.current_score}', align='center', font=FONT_STYLE)

    def game_over(self):
        ''' print the "GAME OVER" at the center of screen '''
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT_STYLE)



