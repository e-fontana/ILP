ENTRIES = int(input())
BALLOONS = list(map(int, input().split()))
LOOSING_POINTS_BALLOON = int(input()) 

POINTS = 0

for x in BALLOONS:
    if x != LOOSING_POINTS_BALLOON:
        POINTS += x
    else:
        POINTS -= x

print(POINTS)