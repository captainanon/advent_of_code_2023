input = 'day_1/puzzle_1.txt'


def solve(input):
    with open(input) as file:
        lst = []
        for line in file.readlines():
            temp = [x for x in line if x.isdigit()]
            first = temp[0]
            last = temp[-1]
            lst.append(int(''.join([first, last])))
    return sum(lst)


if __name__ == '__main__':
    print(solve(input)) # 54968