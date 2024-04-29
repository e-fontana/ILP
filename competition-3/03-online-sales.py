itens = int(input())
total = 0
for x in range(itens):
    q, v = map(float, input().split())
    total += q * v
print(f'{total:.2f}')
