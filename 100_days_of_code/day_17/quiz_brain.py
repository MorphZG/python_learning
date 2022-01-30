'''
questioning and quiz funcionality will go here
- asking the questions
- checking if the answer was correct
- checking if we're the end of the quiz
'''


class QuizBrain:
    '''main quiz funcionality'''

    def __init__(self, question_list):
        '''initialize attributes'''
        self.question_number = 0  # current question
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        '''return boolean depending on the value of question_number'''
        return self.question_number < len(self.question_list)

    def next_question(self):
        '''
        get question object at current question_number from from the question_list
        use input() to show the user Question['text'] and ask for the answer
        modify self.question_number += 1
        '''
        current_question = self.question_list[self.question_number]  # get Question object from question_list
        text = current_question.text  # Question object have self.text and self.answer attributes
        prefix = f"Q.{self.question_number+1}:"  # question format Q.1: This is the first question?
        user_answer = input(f"{prefix} {text} (True/False)? ")  # print formated question and store the answer
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        ''' compare user_answer and correct_answer '''
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.user_score += 1
        else:
            print("That's wrong!")

        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.user_score}/{self.question_number}')
        print('\n')  # empty line between questions

