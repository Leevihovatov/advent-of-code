def main():
    with open("input09.txt", "r") as f:
        data = [int(x) for x in list(f.read())]

    file_id = 0
    unzipped = []
    for i,d in enumerate(data):
        if i % 2 == 0:
            unzipped += [file_id]*d
            file_id += 1
        else:
            unzipped += ['.']*d
    
    unzipped2 = unzipped.copy()

    compact = False

    # Silver move files
    while not compact:
        try:
            empty = unzipped.index('.')
            unzipped[empty] = unzipped[-1]
            unzipped.pop(-1)
        except:
            compact = True

    silver = sum([i*x for i,x in enumerate(unzipped)])

    empty_spaces = [] # what are we living for?

    # Find empty spaces and their size
    n = 0
    pos = 0
    for i,u in enumerate(unzipped2):
        if u == '.':
            if n == 0:
                pos = i
            n += 1
        else:
            if n > 0:
                empty_spaces.append([pos,n])
            n = 0

    counts = data[::2]

    # Gold move files
    for i in reversed(range(len(counts))):
        pos = unzipped2.index(i)
        n = unzipped2.count(i)
        for j,e in enumerate(empty_spaces):
            if counts[i] <= e[1] and e[0] < pos:
                
                for m in range(pos,pos+counts[i]):
                    unzipped2[m] = '.'
                for c in range(counts[i]):
                    unzipped2[e[0]+c] = i
                if counts[i] == e[1]:
                    empty_spaces.pop(j)
                else:
                    empty_spaces[j] = [e[0]+counts[i], e[1]-counts[i]]
                
                break

    unzipped2 = [x if type(x) == int else 0 for x in unzipped2]
    gold = sum([i*x for i,x in enumerate(unzipped2)])

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()