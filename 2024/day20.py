def main():
    with open("input20.txt", "r") as f:
        data = f.read().splitlines()
    
    for i,d in enumerate(data):
        for j,c in enumerate(d):
            if c == 'S':
                pos = [i,j]

    silver = 0
    gold = 0

    path = [pos]
    finished = False
    # Find the no-cheat path and save the path indices
    while not finished:
        candidates = []    
        last = path[-1]
        candidates = [[last[0]-1,last[1]], [last[0],last[1]+1], [last[0]+1,last[1]], [last[0],last[1]-1]]
        for c in candidates:
            if data[c[0]][c[1]] == 'E':
                path.append(c)
                finished = True
                break
            elif data[c[0]][c[1]] == '.' and [c[0],c[1]] not in path:
                path.append(c)
                break

    save = 100
    silver_cheat = 2
    gold_cheat = 20

    # For each step in the path:
    # Check path steps over 100 steps forward (needed timesave)
    # If the step is reachable in distance less than cheat time then good cheat
    # Need to subtract used cheat time from cheated step amount and do some other index things
    for i in range(len(path)-save-1):
        for j in range(i+save, len(path)):
            used = abs(path[i][0]-path[j][0]) + abs(path[i][1]-path[j][1])
            if used <= gold_cheat and j-i-used >= save:
                gold += 1
                if used <= silver_cheat:
                    silver += 1 
                
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()