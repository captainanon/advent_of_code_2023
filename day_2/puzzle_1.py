input = 'day_2/input.txt'
red = 12
green = 13
blue = 14


def solve(input):
    count = 0
    with open(input) as file:
        for game, line in enumerate(file.readlines()):
            line = line.split(' ')
            for idx, x in enumerate(line):
                if x.startswith('red'):
                    if int(line[idx-1]) > red:
                        break
                elif x.startswith('green'):
                    if int(line[idx-1]) > green:
                        break
                elif x.startswith('blue'):
                    if int(line[idx-1]) > blue:
                        break
                if idx == len(line) - 1:
                    count += game + 1
    return count


if __name__ == '__main__':
    print(solve(input)) # 2101