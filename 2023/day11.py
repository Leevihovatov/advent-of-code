def main():
    with open("input11.txt", "r") as f:
        data = f.read().splitlines()
        
    empty_columns = [x for x in range(len(data[0]))]
    empty_rows = [x for x in range(len(data[0]))]
    
    # Remove indexes from the empty_columns and empty_rows
    # so that only the empty ones remain
    # Also get the coordinates of the galaxies (non-expanded universe)
    galaxies = []
    for i,line in enumerate(data):
        if line.count('#') != 0:
            empty_rows.remove(i)
            for j,c in enumerate(line):
                if c == '#':
                    galaxies.append([i,j])
                    try:
                        empty_columns.remove(j)
                    except:
                        pass
    # Calculate galaxy-wise distances
    def galaxy_distances(expanded):   
        total = 0
        for i,g in enumerate(galaxies):
            for j in range(i+1,len(galaxies)):
                plus = 0
                gc = [galaxies[i][1],galaxies[j][1]]
                gr = [galaxies[i][0],galaxies[j][0]]
                # Check if empty columns/rows are in between galaxies and add to distance accordingly
                for ec in empty_columns:
                    if ec in range(min(gc)+1,max(gc)):
                        plus += expanded
                for er in empty_rows:
                    if er in range(min(gr)+1,max(gr)):
                        plus += expanded
                total += abs(gr[0]-gr[1])+abs(gc[0]-gc[1])+plus
        return total
    
    silver = galaxy_distances(1)
    gold = galaxy_distances(999999)
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()