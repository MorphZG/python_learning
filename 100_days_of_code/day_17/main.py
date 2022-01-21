from data import question_data
from question_model import Question
from quiz_brain import *


#new_question = Question('2+3=5', True)
#print(new_question)

# create list of question objects
# i will use Question() class from question_model.py
# and generate question objects from question_data.py
question_bank = []
for question in question_data:
    question_object = Question(question['text'], question['answer'])
    question_bank.append(question_object)

# building QuizBrain instance
main_quiz = QuizBrain(question_bank)
main_quiz.next_question()

# construct a while loop that will throw questions as long as user gives
# correct answer. the loop ends when there is no more questions or user
# gives wrong answer.
while main_quiz.still_has_questions():
    main_quiz.next_question()

# CONTINUE at video 158, min 01:00 
#tags: class, list dictionary objects, modules
