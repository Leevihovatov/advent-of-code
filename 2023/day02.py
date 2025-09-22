def main():
    with open("input02.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    def find_max_cubes(line):
        # Make lists of the lines and get the numbers that correspond to colours
        line = line.replace(':','').replace(',','').replace(';','').split(' ')
        red_indices = [i-1 for i, x in enumerate(line) if x == "red"]
        green_indices = [i-1 for i, x in enumerate(line) if x == "green"]
        blue_indices = [i-1 for i, x in enumerate(line) if x == "blue"]

        # Get the maximum number of cubes for each colour in game
        max_red_cubes = max([int(line[i]) for i in red_indices])
        max_green_cubes = max([int(line[i]) for i in green_indices])
        max_blue_cubes = max([int(line[i]) for i in blue_indices])
        
        return [int(line[1]), max_red_cubes, max_green_cubes, max_blue_cubes]

    max_cubes = []
    for line in data:
        max_cubes.append(find_max_cubes(line))

    # Make a list of possible games and their game-indices
    possible = list(filter(lambda x: x[1] <= 12 and x[2] <= 13 and x[3] <= 14, max_cubes))
    possible = list(map(lambda x: x[0],possible))

    # Today easy 2nd part just adding this as I already had a list of the max cubes
    powers = list(map(lambda x: x[1]*x[2]*x[3],max_cubes))

    silver = sum(possible)
    gold = sum(powers)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()