data = list(map(int, input().split()))

classification = {
    "marrom": 120,
    "azul": 110,
    "verde": 90,
    "roxa": 72,
    "amarela": 60,
}
if data[0] < 1:
    print("branca")
else:
    for color, value in classification.items():
        if data[1] >= value:
            print(color)
            break
