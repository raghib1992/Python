class QuizBrain:
    
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        question_text = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_text.text}. (True/False)?: ")
        self.check_answer(user_answer,question_text.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Correct answer is was {correct_answer}")
        print(f"Your score is {self.score}/{len(self.question_list)}")
        