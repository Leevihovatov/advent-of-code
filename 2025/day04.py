# I want to do these with plain python, so not using ready convolution functions from packages

def main():
    with open("input04.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    padded_data = []

    for d in data:
        padded = '.'+d+'.'
        bin_str = padded.replace('.', '0').replace('@', '1')
        bin_int = [int(x) for x in list(bin_str)]
        padded_data.append(bin_int)

    padded_data.insert(0, [0]*len(padded_data[0]))
    padded_data.append([0]*len(padded_data[0]))

    dirs = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]

    rows = len(padded_data)
    columns = len(padded_data[0])

    rolls = 0
    counts = []
    
    while True:
        removables = []
        
        for i in range(1, rows-1):
            for j in range(1, columns-1):
                if padded_data[i][j] == 1:
                    for d in dirs:
                        if padded_data[i+d[0]][j+d[1]] == 1:
                            rolls += 1
                    if rolls < 4:
                        removables.append((i, j))
                rolls = 0

        if removables == []:
            break

        counts.append(len(removables))
        for r in removables:
            padded_data[r[0]][r[1]] = 0

    silver = counts[0]
    gold = sum(counts)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()