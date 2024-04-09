selection = int(input())
menus = [
    "HAMBURGUER VEGANO, CHURRASCO VEGANO E COXINHA VEGANA",
    "HAMBURGUER, CHURRASCO E COXINHA"
]
if selection == 1:
    print(menus[0])
elif selection == 2:
    print(menus[1])
elif selection == 3:
    print(*menus, sep="\n")
