eggs = int(input())
colors = {
    "vermelho": 0,
    "azul": 0,
    "amarelo": 0,
}
for x in range(eggs):
    colors[list(colors.keys())[x % 3]] += 1
print(f"Vermelho {colors['vermelho']}\nAzul {colors['azul']}\nAmarelo {colors['amarelo']}")