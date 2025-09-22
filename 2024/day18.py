def main():
    with open("input18.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    dim = 71
    max_dim = dim-1
    n_bits = 1024

    grid = []
    for i in range(dim):
        grid.append(['.']*dim)

    for n in range(n_bits,len(data)):

        # Create grid with n fallen bits
        for i in range(n):
            d = data[i]
            grid[int(d.split(',')[1])][int(d.split(',')[0])] = '#'
        
        # Find path
        paths = [[[0,0]]] # All tracked paths
        min_steps = {} # Min steps to reach certain cell
        full_path = []
        while full_path == []:

            new_paths = []
            candidates = []

            if paths == []:
                gold = data[n]
                break
                
            for p in paths:

                # Go to 4 cardinal directions from the end of the path
                last = p[-1]
                candidates = [[last[0]-1,last[1]], [last[0],last[1]+1], [last[0]+1,last[1]], [last[0],last[1]-1]]
                for c in candidates:
                    # If in bounds of the area
                    if c[0] >= 0 and c[0] <= max_dim and c[1] >= 0 and c[1] <= max_dim:

                        # If at the end
                        if c == [max_dim, max_dim]:
                            full_path = p+[c]
                            break
                        # If not blocked cell
                        elif grid[c[0]][c[1]] == '.' and [c[0],c[1]] not in p:
                            # Keep tracking the path if the cell has not been reached with this few steps
                            # If it has already been reached with fewer steps, don't keep tracking that path
                            if str(c) in min_steps:
                                if len(p) < min_steps[str(c)]:
                                    min_steps[str(c)] = len(p)
                                    new_paths.append(p+[c])
                            else:
                                    min_steps[str(c)] = len(p)
                                    new_paths.append(p+[c])
                
                if full_path != []:
                    break

            paths = new_paths

        steps = len(full_path)-1
        
        if n == n_bits:
            silver = steps

        if steps == -1:
            gold = data[n-1]
            break

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()