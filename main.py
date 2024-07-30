n = int(input('Что-то на древнем...3...20' ))

result = []

for i in range(1, 21):
    for j in range(1, 21):
        if n % (i + j) == 0 and i < j and (i + j) != 0:
            result.append(str(i))
            result.append(str(j))
print(''.join(result))