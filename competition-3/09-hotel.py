guests = int(input())
rooms = {
    'Casal': 2,
    'Triplo': 3,
    'Quadruplo': 4,
    'Familia': 5,
}
people_available = 0
while True:
    room = input()
    if room == 'FIM':
        break
    if room in rooms:
        people_available += rooms[room]
if people_available >= guests:
    print("Pode reservar! Esses quartos cabem todos.")
else:
    print("Procure outra pousada.")