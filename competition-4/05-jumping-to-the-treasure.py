ENTRIES = int(input())
OBSTACLES_HEIGHT = list(map(int, input().split()))
MAX_HEIGHT = int(input())

PASSED = 0

for x in OBSTACLES_HEIGHT:
    if x <= MAX_HEIGHT:
        PASSED += 1
    else:
        break

print(PASSED, int(PASSED == ENTRIES), sep='\n')
