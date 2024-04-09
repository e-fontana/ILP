op = str(input())
nums = list(map(int, input().split()))

if op == '+':
    print(f'soma: {nums[0] - nums[1]}')
elif op == '-':
    print(f'subtracao: {nums[0] - nums[1]}')
elif op == '*':
    print(f'multiplicacao: {nums[0] * nums[1]}')
elif op == '/':
    if nums[1] == 0:
        print('erro: divisao por zero')
    else:
        print(f'divisao: {nums[0] // nums[1]}')
