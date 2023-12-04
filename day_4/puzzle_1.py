input = 'day_4/input.txt'


def solve(input):
    scores = []
    with open(input) as file:
        for line in file:
            line = line.strip('\n')
            line = line.split('|')
            winning_nums = [int(x) for x in line[0].split(':')[1].strip().split()]
            my_nums = [int(x) for x in line[1].strip().split()]
            temp = []
            for num in my_nums:
                if num in winning_nums:
                    temp.append(num)
            if len(temp) > 0:
                x = 1
                i = 1
                while i < len(temp):
                    x *= 2
                    i += 1
                scores.append(x)
    return sum(scores)
                

if __name__ == '__main__':
    print(solve(input)) # 21158