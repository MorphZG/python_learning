'''
create question objects with attributes text and answer
'''


class Question:
    '''Question class'''

    def __init__(self, question_text, question_answer):
        '''initialize question object'''
        self.text = question_text
        self.answer = question_answer

