input = 'day_6/input.txt'


def solve(input):
    with open(input) as file:
        times = list(map(int, file.readline().strip().split(':')[1].split()))
        distances = list(map(int, file.readline().strip().split(':')[1].split()))
        product = 1
        for idx, time in enumerate(times):
            i = 0
            count = 0
            while i <= time:
                speed = i
                remaining_time = time - i
                traveled_distance = speed * remaining_time
                if traveled_distance > distances[idx]:
                    count += 1
                i += 1
            product *= count
    return product

               
if __name__ == '__main__':
    print(solve(input)) # 1155175