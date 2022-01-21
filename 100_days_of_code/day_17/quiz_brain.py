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


    def still_has_questions(self):
        # CONTINUE - video 158, min 01:00
        '''return boolean depending on the value of question_number'''
        pass

    def next_question(self):
        '''
        retrieve the item at the current question_number from the question_list
        use input() to show the user Question['text'] and ask for the answer
        modify self.question_number += 1
        '''
        current_question = self.question_list[self.question_number]  # get Question object from question_list
        text = current_question.text  # Question object have self.text and self.answer attributes
        prefix = f"Q.{self.question_number+1}:"  # question format Q.1: This is the first question?
        answer = input(f"{prefix} {text} (True/False)? ")
        self.question_number += 1


