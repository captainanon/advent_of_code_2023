import copy


def tilt(mirrors):
    r = len(mirrors)
    c = len(mirrors[0])
    i = 1
    while i < r:
        j = 0
        while j < c:
            if mirrors[i][j] == 'O':
                k = i
                while k > 0:
                    if mirrors[k-1][j] == '.':
                        mirrors[k-1][j] = 'O'
                        mirrors[k][j] = '.'
                        k -= 1
                    else:
                        break
            j += 1
        i += 1
    return mirrors


def calc_load(mirrors):
    load = 0
    r = len(mirrors)
    c = len(mirrors[0])
    i = 0
    while i < r:
        j = 0
        while j < c:
            if mirrors[i][j] == 'O':
                load += r - i
            j += 1
        i += 1
    return load


def find_total_cycles(n, mirrors):
    cache_ = []
    for x in range(0, n):
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        if mirrors in cache_:
            period_list = [idx for idx, val in enumerate(cache_) if val == mirrors]
            if len(period_list) > 1:
                init_cycles = period_list[0] + 1
                period = period_list[1] - period_list[0]
                additon_cycles = (n - init_cycles) % period
                total_cycles = init_cycles + period + additon_cycles
                return total_cycles
        cache_.append(copy.deepcopy(mirrors))


def solve(n, mirrors):
    for x in range(0, n):
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
        mirrors = tilt(mirrors)
        mirrors = [list(x) for x in map(reversed, zip(*mirrors))]
    load = calc_load(mirrors)
    return load
       

input = 'day_14/input.txt'
with open(input) as file:
    mirrors = [[x for x in y] for y in file.read().splitlines()]
n = 1000000000
total_cycles = find_total_cycles(n, copy.deepcopy(mirrors))
solution = solve(total_cycles, mirrors)
print(solution) # 104409