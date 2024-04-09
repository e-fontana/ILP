data = list(map(str, input().split()))
nome = data[0]
conditions = {
    'idade minima': int(data[1]) >= 12 and int(data[1]) <= 100,
    'bussola': bool(int(data[2])),
    'mapa do tesouro': bool(int(data[3])),
    'po magico': bool(int(data[4])),
    'espada magica': bool(int(data[5]))
}
if all(value is True for value in conditions.values()):
    print(f'{nome}, condicoes ok! Boa sorte na busca pelo tesouro!')
else:
    lista = []
    for key, value in conditions.items():
        if value is not True:
            lista.append(f'Nao possui {key};')
    print(*lista)
    print(f'{nome} nao cumpre todas as condicoes!')
