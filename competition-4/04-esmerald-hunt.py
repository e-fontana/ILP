box_number = int(input())
boxes = map(int, input().split())
chaos = int(input())
if chaos in boxes:
    print(chaos)
else:
    print(-1)
