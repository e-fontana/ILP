def calc_date(date):
    return abs(int(date) - 2023) * 2

a, b, c, d, e, f = map(calc_date, input().split())

print(f'Luther {a}')
print(f'Diego {b}')
print(f'Alisson {c}')
print(f'Klaus {d}')
print(f'Five {a + b + c + d + e + f}')
print(f'Ben {e}')
print(f'Viktor {f}')
