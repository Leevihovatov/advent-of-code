def main():
    with open("input05.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    ranges = data[:data.index('')]
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]
    ranges = sorted(ranges, key=lambda x: x[0])

    ids = data[data.index('')+1:]
    ids = [int(id) for id in ids]

    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                silver += 1
                break

    # Combining ranges, ranged array is already ordered by start of ranges
    unique_ranges = []
    start = None
    stop = None
    for r in ranges:
        if not start:
            start = r[0]
            stop = r[1]
        else:
            if r[0] >= start and r[0] <= stop:
                if r[1] > stop:
                    stop = r[1]
            else:
                unique_ranges.append((start, stop))
                start = r[0]
                stop = r[1]

    unique_ranges.append((start, stop))

    for u in unique_ranges:
        gold += u[1] - u[0] + 1  

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()