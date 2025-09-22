def main():
    with open("input05.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    seeds = data[0].split()[1:]
    del(data[0])

    # Putting the seeds and ranges to two arrays for part 2
    seeds_start = []
    seeds_range = []
    for i in range(0,len(seeds),2):
        seeds_start.append(seeds[i])
        seeds_range.append(seeds[i+1])

    min_location = 99999999999999999999999999999999999999999999 # :D

    # Part 1: Go through seeds one by one and map them to the maps
    # using comparator operators and calculating the start and end of ranges
    for seed in seeds:
        new_source = seed
        for map in data:
            source = new_source
            map = map.splitlines()
            del(map[0])
            found = False
            for line in map:
                l = line.split()
                if int(source) >= int(l[1]) and int(source) <= int(l[1])+int(l[2])-1:
                    source_index = int(source)-int(l[1])
                    new_source = int(l[0])+source_index
                    found = True
            if not found:
                new_source = int(source)
        if new_source < min_location:
            min_location = new_source

    silver = min_location

    min_location = 99999999999999999999999999999999999999999999 # :D
    # Part 2: If a group of seeds goes through the exact same mapping till the location
    # we can say that only the smallest of those seeds is worth mapping
    # That group of seeds is calculated by taking the minimum of group going through any mapping for that seed
    # The group size is calculated by how far away the current seed mapping is from the end of the range for that mapping

    for i in range(len(seeds_start)):
        checked_range = 0 # How many seeds are checked from the current seed range
        min_package = 0 # Used for how many seed go through the exact same mapping (0 used for first time because line 52)
        while checked_range < int(seeds_range[i]):
            checked_range += min_package
            if checked_range > int(seeds_range[i]):
                break # The not wanted additional loop. Range here is over the seed range
            new_source = int(seeds_start[i])+checked_range
            min_package = 999999999999999999999999999999999999 # :D
            
            for map in data:
                source = new_source
                map = map.splitlines()
                del(map[0])
                found = False
                for line in map:
                    l = line.split()
                    if int(source) >= int(l[1]) and int(source) <= int(l[1])+int(l[2])-1:
                        source_index = int(source)-int(l[1])
                        # Calculate the group size going through current mapping
                        current_package = int(l[2])-source_index
                        if current_package < min_package:
                            min_package = current_package
                        new_source = int(l[0])+source_index
                        found = True
                if not found:
                    new_source = int(source)
                    # Forgot to check the group here, happened to work for my input without
            if new_source < min_location:
                min_location = new_source

    gold = min_location

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()