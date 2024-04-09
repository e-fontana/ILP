min_grade = float(input())
grade1 = float(input())
grade2 = float(input())
average = (grade1 + grade2) / 2
if average >= min_grade:
    print(f'Aluno aprovado na disciplina! Parabens! A sua media foi: {average:.2f}')
