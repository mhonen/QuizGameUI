#********************************************************************
#
# main.py
#********************************************************************

#To access various classes
from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [] # List to hold the questions
#Add questions to question_bank list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
 
quiz = QuizBrain(question_bank) # Get access to quiz_brain controller (Kind of like a Game Controller)
quiz_ui = QuizInterface(quiz) # Get access to start the user interface with quiz (QuizBrain) passed to UI class.

