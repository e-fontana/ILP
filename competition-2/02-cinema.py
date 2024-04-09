category = str(input())
categories = {
    'idoso': 'gratuidadde',
    'estudante': '10 reais',
    'outros': '20 reais',
    'casadinha': '30 reais',
    'trio': '40 reais',
}
if category in categories:
    print(categories[category])
else:
    print(categories['outros'])
