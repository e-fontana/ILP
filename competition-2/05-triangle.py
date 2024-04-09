A1 = int(input())
A2 = int(input())
A3 = int(input())

if A1 + A2 + A3 != 180:
    print('Nao eh triangulo!')
elif A1 == 90 or A2 == 90 or A3 == 90:
    print('Triangulo Retangulo!')
elif A1 > 90 or A2 > 90 or A3 > 90:
    print('Triangulo Obtusangulo!')
elif A1 < 90 and A2 < 90 and A3 < 90:
    print('Triangulo Acutangulo!')
