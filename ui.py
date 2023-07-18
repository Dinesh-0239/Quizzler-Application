from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        """Setup GUI"""
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.iconbitmap("AppIcon.ico")
        self.window.resizable(False,False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Getting the next question on the canvas"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            """"display next question"""
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            """display message when question ends"""
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            """disable buttons when questions not left"""
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """return feedback whether your choice is correct or not"""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """return feedback whether your choice is correct or not"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """change color of the canvas according to the answer"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        #after 1 sec proceed to the next question
        self.window.after(1000, self.get_next_question)








