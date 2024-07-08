NINJAS = int(input())
BATTLE_FRONT = list(map(int, input().split()))
for i, x in enumerate(reversed(BATTLE_FRONT)):
    print(f'{len(BATTLE_FRONT) - i}: {x}')