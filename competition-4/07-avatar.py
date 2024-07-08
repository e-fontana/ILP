ENTRIES = int(input())
HABILITY = list(map(int, input().split()))
IDS = list(map(int, input().split()))
ELEMENT = int(input())

OUTPUT = []

for i, x in enumerate(HABILITY):
    if x == ELEMENT:
        OUTPUT.append(IDS[i])

print(*OUTPUT) if len(OUTPUT) > 0 else print("Nenhum")