ENTRIES = int(input())
MONEY_EARNED = list(map(int, input().split()))
MULTIPLIER = int(input())
print(*(x * MULTIPLIER for x in MONEY_EARNED))
