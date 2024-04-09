moves = list(map(str, input().split()))
available_moves = ["direita", "esquerda"]
moves = [available_moves.index(moves[0]), available_moves.index(moves[1])]
if moves == [0, 1]:
    print("Achou")
elif moves == [1, 1]:
    print("Morreu")
else:
    print('Tente novamente')
