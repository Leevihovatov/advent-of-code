import copy
def main():
    with open("input06.txt", "r") as f:
        data = f.read().splitlines()

    silver = 0
    gold = 0

    # Array for marking positions visited by the guard in silver
    visited = []
    for i,line in enumerate(data):
        visited.append([0]*len(line))
        data[i] = list(line)
        for j,c in enumerate(line):
            if c == '^':
                guard_pos = [i,j]
    
    start_pos = guard_pos

    visited[guard_pos[0]][guard_pos[1]] = 1

    # Get direction of straight movement or turning from the facing direction of the guard
    def get_dir(facing):
        match facing:
            case '^':
                move_dir = [-1, 0]
                turn_dir = [0, 1]
                turn_face = '>'
            case '>':
                move_dir = [0, 1]
                turn_dir = [1, 0]
                turn_face = 'v'
            case 'v':
                move_dir = [1, 0]
                turn_dir = [0, -1]
                turn_face = '<'
            case '<':
                move_dir = [0, -1]
                turn_dir = [-1, 0]
                turn_face = '^'
        return move_dir, turn_dir, turn_face
    
    # Move the guard in the grid and mark positions visited 1
    in_area = True
    while in_area:
        facing = data[guard_pos[0]][guard_pos[1]]
        move_dir, turn_dir, turn_face = get_dir(facing)

        try:
            if data[guard_pos[0]+move_dir[0]][guard_pos[1]+move_dir[1]] == '.': # Moving to empty space

                data[guard_pos[0]][guard_pos[1]] = '.'
                guard_pos = [guard_pos[0]+move_dir[0], guard_pos[1]+move_dir[1]]
                data[guard_pos[0]][guard_pos[1]] = facing
                visited[guard_pos[0]][guard_pos[1]] = 1

            else: # Obstacle, turn right

                data[guard_pos[0]][guard_pos[1]] = '.'
                guard_pos = [guard_pos[0]+turn_dir[0], guard_pos[1]+turn_dir[1]]
                data[guard_pos[0]][guard_pos[1]] = turn_face
                visited[guard_pos[0]][guard_pos[1]] = 1
        except:
            in_area = False
    
    for line in visited:
        silver += sum(line)

    data[guard_pos[0]][guard_pos[1]] = '.'

    # Go through visited positions and put obstacle in them
    # Move guard through the space and check if there is loop
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[start_pos[0]][start_pos[1]] = '^'
            guard_pos = start_pos
            if data[i][j] in ['#', '^']:
                continue
            elif visited[i][j] == 1:
                data[i][j] = '#'

                # Add visited position to string for checking being in loop
                visited_str = str(guard_pos)

                in_area = True
                in_loop = False
                while in_area and not in_loop:

                    facing = data[guard_pos[0]][guard_pos[1]]

                    move_dir, turn_dir, turn_face = get_dir(facing)

                    next_y = guard_pos[0]+move_dir[0]
                    next_x = guard_pos[1]+move_dir[1]
                    if (next_y < 0) or (next_y >= len(data)) or (next_x < 0) or (next_x >= len(data[0])):
                        in_area = False
                    else:
                        if data[guard_pos[0]+move_dir[0]][guard_pos[1]+move_dir[1]] == '.': # Moving to empty space
                            path = str(guard_pos)
                            data[guard_pos[0]][guard_pos[1]] = '.'
                            guard_pos = [guard_pos[0]+move_dir[0], guard_pos[1]+move_dir[1]]
                            path += str(guard_pos)
                            # If 2 consecutive positions are already in the string then in loop
                            if path in visited_str:
                                in_loop = True
                                gold += 1
                            visited_str += str(guard_pos)
                            data[guard_pos[0]][guard_pos[1]] = facing
                    
                        else: # Obstacle, turn right
                            next_y = guard_pos[0]+turn_dir[0]
                            next_x = guard_pos[1]+turn_dir[1]
                            if (next_y < 0) or (next_y >= len(data)) or (next_x < 0) or (next_x >= len(data[0])):
                                in_area = False
                            else:
                                path = str(guard_pos)
                                data[guard_pos[0]][guard_pos[1]] = '.'

                                # 180 turn
                                if data[guard_pos[0]+turn_dir[0]][guard_pos[1]+turn_dir[1]] == '#':
                                    move_dir, turn_dir, turn_face = get_dir(turn_face)
                                    guard_pos = [guard_pos[0]+turn_dir[0], guard_pos[1]+turn_dir[1]]
                                    path += str(guard_pos)
                                    if path in visited_str:
                                        in_loop = True
                                        gold += 1
                                    visited_str += str(guard_pos)
                                    data[guard_pos[0]][guard_pos[1]] = turn_face
                                # Only 90 turn
                                else:    
                                    guard_pos = [guard_pos[0]+turn_dir[0], guard_pos[1]+turn_dir[1]]
                                    path += str(guard_pos)
                                    if path in visited_str:
                                        in_loop = True
                                        gold += 1
                                    visited_str += str(guard_pos)
                                    data[guard_pos[0]][guard_pos[1]] = turn_face

                data[i][j] = '.'
                data[guard_pos[0]][guard_pos[1]] = '.'
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()