#***************************************************************************************
#
# ui.py
# Remarks: This is the workhorse that gives the user a GUI to answer the questions
#**************************************************************************************

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    #Constructor and main loop for the GUI
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("My Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 
                                                     125,
                                                     width=280,
                                                     text="Some Question Text", 
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    # Retrieves next question.  Also stops the program when all ten questions are answered    
    def get_next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Your've reached the end of the test")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    # Instatiates when true button is pressed    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    # Instatiates when false button is pressed 
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    #Gives user correct feedback if given right or wrong answer    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green") #change canvas color
        else:
            self.canvas.config(bg="red")
        #Set timer for 1 second, then calls get_next_question (canvas color will change back inside get_next_question function)    
        self.window.after(1000, self.get_next_question)    
        
        