#------------------------------------------------------------Quizzler Application-------------------------------------------------------------#

"""
Date: July, 18 2023
Developer : Dinesh Singh

Description: This is the improvement of my previous quiz game which is based on true and false questions here I use Python's Tkinter for gui and requests module direct communicate to api for quiz questions.
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#create empty question bank for hoding questions
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#pass question bank to the Quiz brain
quiz = QuizBrain(question_bank)
#Creating GUI and all the functionality
quiz_ui = QuizInterface(quiz)
