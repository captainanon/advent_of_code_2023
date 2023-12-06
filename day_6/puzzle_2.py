input = 'day_6/input.txt'


def solve(input):
    with open(input) as file:
        time = int(''.join(file.readline().strip().split(':')[1].split()))
        distance = int(''.join(file.readline().strip().split(':')[1].split()))
        i = 0
        count = 0
        while i <= time:
            speed = i
            remaining_time = time - i
            traveled_distance = speed * remaining_time
            if traveled_distance > distance:
                count += 1
            i += 1
    return count

               
if __name__ == '__main__':
    print(solve(input)) # 35961505