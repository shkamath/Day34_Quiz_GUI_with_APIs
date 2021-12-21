from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # self.window.minsize(width=350,height=400)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="sample text", fill=THEME_COLOR, font=("Arial", 25, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label = Label(text="Score: 0", font=(
            "Courier", 15, "normal"), fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.label.grid(row=0, column=1)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0,command=self.set_True)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0,command=self.set_False)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def set_True(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def set_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)    

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
