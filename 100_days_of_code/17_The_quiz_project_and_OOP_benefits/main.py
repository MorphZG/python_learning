from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# new_question = Question('2+3=5', True)
# print(new_question)

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

# while loop throws questions as long as there are questions in the list
while main_quiz.still_has_questions():
    main_quiz.next_question()

# after loop is done, print the following statements:
# "You've completed the quiz"
# "Your final score was: {main.quiz.score} / {number of questions}
print("You've completed the quiz.")
print(f"Your final score was: {main_quiz.user_score}/{len(question_bank)}")



#tags: class, list dictionary objects, modules
