matches = int(input())
albert = [0, 0]
bruno = [0, 0]
for x in range(matches):
    kills, deaths = map(int, input().split())
    albert[0] += kills
    albert[1] += deaths
for x in range(matches):
    kills, deaths = map(int, input().split())
    bruno[0] += kills
    bruno[1] += deaths
kd_albert = albert[0] / albert[1]
kd_bruno = bruno[0] / bruno[1]
if kd_albert > kd_bruno:
    print('Parabens Alberto!')
    print(f'{kd_albert:.2f}')
elif kd_bruno > kd_albert:
    print('Parabens Bruno!')
    print(f'{kd_bruno:.2f}')
else:
    print('Empate')
