total = 0
end = False
i = 0
while not end:
    num = int(input())
    if num <= 0:
        end = True
    else:
        total += num
        i += 1
print(total, i, sep='\n')