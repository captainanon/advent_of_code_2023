input = 'day_5/input.txt'


def solve(input):
    lowest_location = 0
    with open(input) as file:
        end = len(file.readlines())
    with open(input) as file:
        i = 0
        line = file.readline().strip('\n')
        while i <= end:
            if line.startswith('seeds:'):
                seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('seed-to-soil map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                seed_to_soil_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('soil-to-fertilizer map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                soil_to_fertilizer_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('fertilizer-to-water map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                fertilizer_to_water_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('water-to-light map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                water_to_light_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('light-to-temperature map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                light_to_temperature_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('temperature-to-humidity map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                temperature_to_humidity_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            if line.startswith('humidity-to-location map:'):
                line = file.readline().strip('\n')
                i += 1
                source = []
                destination = []
                while line != '':
                    line = [int(x) for x in line.split(' ')]
                    source.append((line[1], line[1]+line[2]-1))
                    destination.append((line[0], line[0]+line[2]-1))
                    line = file.readline().strip('\n')
                    i += 1
                humidity_to_location_map = dict(zip(source, destination))
                line = file.readline().strip('\n')
                i += 1
                continue
            line = file.readline().strip('\n')
            i += 1
    for seed in seeds:
        for k, v in seed_to_soil_map.items():
            if seed >= k[0] and seed <= k[1]:
                soil = (seed - k[0]) + v[0]
                break
            else:
                soil = seed
        for k, v in soil_to_fertilizer_map.items():
            if soil >= k[0] and soil <= k[1]:
                fertilizer = (soil - k[0]) + v[0]
                break
            else:
                fertilizer = soil
        for k, v in fertilizer_to_water_map.items():
            if fertilizer >= k[0] and fertilizer <= k[1]:
                water = (fertilizer - k[0]) + v[0]
                break
            else:
                water = fertilizer
        for k, v in water_to_light_map.items():
            if water >= k[0] and water <= k[1]:
                light = (water - k[0]) + v[0]
                break
            else:
                light = water
        for k, v in light_to_temperature_map.items():
            if light >= k[0] and light <= k[1]:
                temperature = (light - k[0]) + v[0]
                break
            else:
                temperature = light
        for k, v in temperature_to_humidity_map.items():
            if temperature >= k[0] and temperature <= k[1]:
                humidity = (temperature - k[0]) + v[0]
                break
            else:
                humidity = temperature
        for k, v in humidity_to_location_map.items():
            if humidity >= k[0] and humidity <= k[1]:
                location = (humidity - k[0]) + v[0]
                break
            else:
                location = humidity
        if lowest_location == 0:
            lowest_location = location
        elif location < lowest_location:
            lowest_location = location
    return lowest_location
               

if __name__ == '__main__':
    print(solve(input)) # 551761867