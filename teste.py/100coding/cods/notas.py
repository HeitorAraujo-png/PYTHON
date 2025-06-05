student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for nomes in student_scores:
    if student_scores[nomes] >= 91:
        student_grades[nomes] = 'Outstanding'
    elif student_scores[nomes] >= 81:
        student_grades[nomes] = 'Exceeds Expectations'
    elif student_scores[nomes] >= 71:
        student_grades[nomes] = 'Acceptable'
    else:
        student_grades[nomes] = 'Fail'
print(student_grades)