def main():
    with open("input14.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    turned = []
    for i,line in enumerate(data):
        data[i] = list(line)
    turned.append(list(map(list, zip(*data))))

    for line in turned[0]:
        cube_rock = len(line)+1
        round_rocks = 0
        for i,c in enumerate(line):
            if line[i] == 'O':
                round_rocks += 1
            elif line[i] == '#' and round_rocks != 0:
                for r in range(1,round_rocks+1):
                    silver += (cube_rock-r)
                cube_rock = (len(line)-(i+1))+1
                round_rocks = 0
            elif line[i] == '#':
                cube_rock = (len(line)-(i+1))+1
        if round_rocks != 0:
            for r in range(1,round_rocks+1):
                silver += (cube_rock-r)
                
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()