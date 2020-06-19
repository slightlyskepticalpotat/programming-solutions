questions = int(input())
student_answers = []
correct_answers = []
questions_correct = 0

for i in range(0, questions):
    student_answers.append(input())

for i in range(0, questions):
    correct_answers.append(input())

for i in range(0, questions):
    if student_answers[i] == correct_answers[i]:
        questions_correct += 1
    else:
        pass
print(questions_correct)