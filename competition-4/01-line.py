passwords = int(input())
odd = []
even = []
for x in range(passwords):
    password = input()
    if int(password) % 2 == 0:
        even.append(password)
    else:
        odd.append(password)
print(*(odd + even), sep='\n')
