def main():
    with open("input15.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    grid = data[0].splitlines()
    moves = "".join(data[1].splitlines())

    for i, row in enumerate(grid):
        grid[i] = list(row)
        for j, col in enumerate(row):
            if col == '@':
                pos = [i,j]

    def get_dir(dir):
        match dir:
            case '^':
                return [-1,0]
            case '>':
                return [0,1]
            case 'v':
                return [1,0]
            case '<':
                return [0,-1]

    for m in moves:
        dir = get_dir(m)
        pos_to_move = [pos[0]+dir[0], pos[1]+dir[1]]
        if grid[pos_to_move[0]][pos_to_move[1]] == '.':
            grid[pos_to_move[0]][pos_to_move[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            pos = pos_to_move
        elif grid[pos_to_move[0]][pos_to_move[1]] == '#':
            continue
        else:
            check_pos = [pos_to_move[0]+dir[0], pos_to_move[1]+dir[1]]
            while True:
                if grid[check_pos[0]][check_pos[1]] == '#':
                    break
                elif grid[check_pos[0]][check_pos[1]] == '.':
                    grid[check_pos[0]][check_pos[1]] = 'O'
                    grid[pos_to_move[0]][pos_to_move[1]] = '@'
                    grid[pos[0]][pos[1]] = '.'
                    pos = pos_to_move
                    break
                else:
                    check_pos = [check_pos[0]+dir[0], check_pos[1]+dir[1]]


    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'O':
                silver += 100*i+j
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()