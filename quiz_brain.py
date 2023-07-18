#import html to unescape html entities
import html

class QuizBrain:

    def __init__(self, q_list):
        """Initialising quiz brain entities"""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """return True/False whether still has question or not."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """return next question if it has"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text) #unescaping html entities from question text
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Check for currect answer"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
