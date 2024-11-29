from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question.get('question')
    answer = question.get('correct_answer')
    new_question = Question(question_text, answer)
    question_bank.append(new_question)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
