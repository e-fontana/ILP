titans = int(input())
soldiers = (titans - 20) // 5
if ((titans - 20) % 5) > 0:
    soldiers += 1
print(soldiers)