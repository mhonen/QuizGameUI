#******************************************************************************************
#
# quiz_brain.pt
# Remarks: I like to think this class is the main controller of the game.  It keeps track
#          questions and the present score
#
#******************************************************************************************

import html

class QuizBrain:
    #Constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    #See if there are anymore questions in the list.  Also, is important to end the program and keep the program
    #from producing any "Out of Bounds" type errors
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Grab next questions
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    #Checks the answer and returns if true or false
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False