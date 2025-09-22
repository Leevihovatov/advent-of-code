def main():
    with open("input10.txt", "r") as f:
        data = f.read().splitlines()
    
    for i,d in enumerate(data):
        data[i] = [int(x) for x in list(d)]

    silver = 0
    gold = 0

    zeroes = []
    for i,d in enumerate(data):
        for j,c in enumerate(d):
            if c == 0:
                zeroes.append([i,j])
    
    max_row = len(data)-1
    max_col = len(data[0])-1

    for z in zeroes:
        paths = [[z]]
        #print(z)
        num = 0
        while num < 9 and len(paths) > 0:
            num += 1
            new_paths = []
            candidates = []
            for p in paths:
                #print(p)
                last = p[-1]
                candidates = [[last[0]-1,last[1]], [last[0],last[1]+1], [last[0]+1,last[1]], [last[0],last[1]-1]]
                for c in candidates:
                    if c[0] >= 0 and c[0] <= max_row and c[1] >= 0 and c[1] <= max_col:
                        if data[c[0]][c[1]] == num:
                            new_paths.append(p+[c])

            paths = new_paths
            #print(f'{num} {pos}')

        #print('*************')
        if num == 9:
            nines = [p[-1] for p in paths]
            silver += len([list(x) for x in set(tuple(x) for x in nines)])
            gold += len(paths)


    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()