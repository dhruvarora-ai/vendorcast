question_prompt = [
    "What color are apples?\na.Red/Green\nb. Purple\nc.Orange\n\n",
    "What color are the bananas?\na. Teal\nb. Magenta\nc. Yellow\n\n",
    "What color are strawberries?\na. Yellow\nb. Red\nc. Blue\n\n"
]

class Question:
    def __init__(self,Question_prompt,Question_answer):
        self.Question_prompt = Question_prompt
        self.Question_answer = Question_answer

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"c"),
    Question(question_prompt[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
           answer = input(question.Question_prompt)
           if answer.lower() == question.Question_answer.lower():
                score+=1
                print("Correct answer")
           else:
                print("Incorrect")
    print("You got",score,"answers correect out of",len(questions))

run_test(questions)