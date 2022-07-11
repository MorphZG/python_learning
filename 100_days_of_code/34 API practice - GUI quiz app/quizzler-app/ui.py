"""
Display everything on screen
"""
from tkinter import *  # aware of bad practice
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # def function(parameter1[: data_type], parameter2[: data_type]):
        self.quiz = quiz_brain  # QuizBrain object available inside QuizInterface
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.score_label = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # canvas
        # when placing text or image on canvas you must provide position
        # IndexError: tuple index out of range
        self.canvas = Canvas(width=300, height=300, bg='white')
        self.canvas_text = self.canvas.create_text(
                            150, 150,
                            width=280,
                            text='question text displayed here',
                            font=('Arial', 20, 'italic'),
                            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        # green_img and red_img doesnt have 'self' before it.
        # keyword self will turn it into a property that can later be modified
        # from anywhere else in the class
        green_img = PhotoImage(file='./images/true.png')
        self.green_button = Button(image=green_img, command=self.green_click)
        self.green_button.grid(column=0, row=2, padx=15, pady=15)

        red_img = PhotoImage(file='./images/false.png')
        self.red_button = Button(image=red_img, command=self.red_click)
        self.red_button.grid(column=1, row=2, padx=15, pady=15)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Reset the canvas background color, call quiz.next_question() and display
        it as canvas text.
        """
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:  # if there is no more questions in question_bank
            self.canvas.itemconfig(self.canvas_text, text='Game Completed!')
            self.green_button.config(state='disabled')
            self.red_button.config(state='disabled')

    def green_click(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def red_click(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        Change canvas color to green if is_right is True. If is_right is False
        change canvas to red. After 1sec call self.get_next_question()
        """
        if is_right:
            self.canvas.config(self.canvas, bg='green')
        else:
            self.canvas.config(self.canvas, bg='red')

        self.window.after(1000, self.get_next_question)