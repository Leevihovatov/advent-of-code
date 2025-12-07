def main():
    with open("input07.txt", "r") as f:
        input = f.read().splitlines()
    
    silver = 0
    gold = 0

    data = []
    for r in input:
        data.append(list(r))

    for i,c in enumerate(data[0]):
        if c == 'S':
            data[0][i] = 1

    rows = len(data)
    columns = len(data[0])

    # Keep track of how many different beams go through each point
    # Kind of a pascal triangle, but taking counts from:
    # - directly above (uninterrupted beam)
    # - sides (NW, NE) in cases where it comes from a split

    for i in range(rows-1):
        for j in range(columns):
            if isinstance(data[i][j], int):
                if data[i+1][j] == '.':
                    data[i+1][j] = data[i][j]
                elif isinstance(data[i+1][j], int):
                    data[i+1][j] += data[i][j]
                elif data[i+1][j] == '^':
                    if isinstance(data[i+1][j-1], int):
                        data[i+1][j-1] += data[i][j]
                    else:
                        data[i+1][j-1] = data[i][j]
                    if isinstance(data[i+1][j+1], int):
                        data[i+1][j+1] += data[i][j]
                    else:
                        data[i+1][j+1] = data[i][j]
                    silver += 1

    # Count the different beams from the lowest level
    for c in data[-1]:
        if isinstance(c, int):
            gold += c

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()