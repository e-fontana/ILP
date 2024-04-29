students = int(input())
grades = {}

for x in range(students):
    name = input()
    n1, n2 = map(float, input().split())
    grades[name] = (n1 * 0.3) + (n2 * 0.7)

print(max(grades, key=grades.get))