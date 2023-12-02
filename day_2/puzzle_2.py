input = 'day_2/input.txt'


def solve(input):
    sum = 0
    with open(input) as file:
        for line in file.readlines():
            line = line.split(' ')
            red = 0
            green = 0
            blue = 0
            for idx, x in enumerate(line):
                if x.startswith('red'):
                    if int(line[idx-1]) > red:
                        red = int(line[idx-1]) 
                elif x.startswith('green'):
                    if int(line[idx-1]) > green:
                        green = int(line[idx-1])
                elif x.startswith('blue'):
                    if int(line[idx-1]) > blue:
                        blue = int(line[idx-1])
            sum += red * green * blue
    return sum


if __name__ == '__main__':
    print(solve(input)) # 58269