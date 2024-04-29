start = int(input())
limit = int(input())
numbers = []
for x in range(start, limit + 1):
    if x % 2 == 0:
        numbers.append(x)
print(*numbers)
print(len(numbers))