def main():
    with open("input25.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    keys = []
    locks = []
    for d in data:
        rows = d.splitlines()
        counts = [-1]*5
        for row in rows:
            for i,c in enumerate(row):  
                if c == '#':
                    counts[i] += 1
        
        if d[0][0] == '#':
            locks.append(counts)
        else:
            keys.append(counts)
    
    for l in locks:
        for k in keys:
            if max([a + b for a, b in zip(l, k)]) <= 5:
                silver += 1


    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()