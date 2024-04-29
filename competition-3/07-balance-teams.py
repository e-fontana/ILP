heroes = int(input())
roles = [0, 0]
for x in range(heroes):
    role = int(input())
    if role in (1, 2):
        roles[role - 1] += 1
if roles[0] > 0 and roles[1] > 0:
    print('Equipe Balanceada')
else:
    print('Equipe Desbalanceada')