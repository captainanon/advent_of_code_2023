# I did not solve this part without help

input = 'day_5/input.txt'


def create_levels_and_mappings(input):
    with open(input) as file:
        end = len(file.readlines())
    with open(input) as file:
        i = 0
        levels_and_mappings = []
        line = file.readline().strip('\n')
        while i <= end:
            if line.startswith('seeds:'):
                seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]
                tups = []
                for i in range(0, len(seeds), 2):
                    tups.append((seeds[i], seeds[i]+seeds[i+1]-1))
                seeds = tups
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
                levels_and_mappings.append(seed_to_soil_map)
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
                levels_and_mappings.append(soil_to_fertilizer_map)
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
                levels_and_mappings.append(fertilizer_to_water_map)
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
                levels_and_mappings.append(water_to_light_map)
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
                levels_and_mappings.append(light_to_temperature_map)
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
                levels_and_mappings.append(temperature_to_humidity_map)
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
                levels_and_mappings.append(humidity_to_location_map)
                line = file.readline().strip('\n')
                i += 1
                continue
            line = file.readline().strip('\n')
            i += 1
    return seeds, levels_and_mappings


def solve(inputs, levels_and_mappings):
    for level in levels_and_mappings:
        next_inputs = []
        while len(inputs) > 0:
            input_start, input_end = inputs.pop()
            for k, v in level.items():
                map_in_start = k[0]
                map_in_end = k[1]
                map_out_start = v[0]
                overlap_start = max(input_start, map_in_start)
                overlap_end = min(input_end, map_in_end)
                if overlap_start <= overlap_end:
                    next_inputs.append((overlap_start - map_in_start + map_out_start, overlap_end - map_in_start + map_out_start))
                    if overlap_start > input_start:
                        inputs.append((input_start, overlap_start - 1))
                    if input_end > overlap_end:
                        inputs.append((overlap_end + 1, input_end))
                    break
            else:
                next_inputs.append((input_start, input_end))
        inputs = next_inputs
    return min(inputs)[0]
               

if __name__ == '__main__':
    seeds, levels_and_mappings = create_levels_and_mappings(input)
    print(solve(seeds, levels_and_mappings)) # 57451709