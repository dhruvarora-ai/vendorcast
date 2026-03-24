class Student:
    def __init__(self, name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
Student1 = Student("Dhruv","Aiml",3.5,True)
Student2 = Student("Rohan","Aids",3.2,True)

print(Student1.is_on_probation)


#quiz
Question_prompts = [
    "What color are apples?\na.Red/Green\nb. Purple\nc.Orange\n\n",
    "What color are the bananas?\na. Teal\nb. Magenta\nc. Yellow\n\n",
    "What color are strawberries?\na. Yellow\nb. Red\nc. Blue\n\n"
]
class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
Questions = [Question(Question_prompts[0],"a"),
             Question(Question_prompts[1],"c"),
             Question(Question_prompts[2],"b")
]

def run_test(Questions):
    score = 0
    for question in Questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            print("Correct Answer")
            score = score+1
        else:
            print("Incorrect Answer")
    print("Your score is",score,"out of",len(Questions))
run_test(Questions)