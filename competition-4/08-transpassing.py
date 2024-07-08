FROGS, STONES = list(map(int, input().split()))

STONES = [0 for x in range(STONES)]
STONES[0] = 1

for x in range(FROGS):
    JUMP_SIZE = int(input())
    MULTIPLES = [JUMP_SIZE * x for x in range(1, len(STONES) + 1)]
    for i, y in enumerate(MULTIPLES):
        if y < len(STONES):
            STONES[y] = 1

print(*STONES)
