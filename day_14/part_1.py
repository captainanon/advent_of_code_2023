input = 'day_14/input.txt'
with open(input) as file:
    mirrors = [[x for x in y] for y in file.read().splitlines()]
count = 0
r = len(mirrors)
c = len(mirrors[0])
i = 0
while i < r:
    j = 0
    while j < c:
        if i == 0 and mirrors[i][j] == 'O':
            count += r - i
        elif mirrors[i][j] == 'O':
            count += r - i
            k = i
            while k > 0:
                if mirrors[k-1][j] == '.':
                    mirrors[k-1][j] = 'O'
                    mirrors[k][j] = '.'
                    count += 1
                    k -= 1
                else:
                    break
        j += 1
    i += 1
print(count) # 113486