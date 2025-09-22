def main():
    with open("input16.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    # Add the edges/directions to starting points
    starts = []
    for i in range(len(data)):
        starts.append([[i,0],[0,1]])
        starts.append([[i,len(data[0])-1],[0,-1]])
    for i in range(len(data[0])):
        starts.append([[0,i],[1,0]])
        starts.append([[len(data)-1,i],[-1,0]])

    # Add the current cell/direction the visited
    def add_visited(current,dir):
        already = visited[current[0]][current[1]]
        if dir in already:
            return False # To not continue this path as it will start to loop
        else:
            visited[current[0]][current[1]].append(dir)
            return True

    # If there is a mirror /,\ or nothing .
    def not_splitter(current,dir):
        current = [current[0]+dir[0],current[1]+dir[1]]
        in_progress[0] = [current,dir]
        return

    # If there is a splitter
    def splitter(current,dir1,dir2):
        current1 = [current[0]+dir1[0],current[1]+dir1[1]]
        current2 = [current[0]+dir2[0],current[1]+dir2[1]]
        in_progress[0] = [current1,dir1]
        in_progress.append([current2,dir2])
        return
    
    silver_answer = False
    for s in starts:
        energized = 0
        current = s[0]
        dir = s[1]

        # To keep track which cells have been visited and what the moving direction has been
        visited = []
        for i in range(len(data)):
            visited.append([[] for i in range(len(data[0]))])

        # Keep count where the beams are currently going, especially when they split
        in_progress = []
        in_progress.append([current,dir])

        # Check the path of the first beam in the all currently splitted while there are still unchecked beam paths
        while in_progress:
            current = in_progress[0][0]
            dir = in_progress[0][1]        
            try:
                if current[0] < 0 or current[1]<0: # If index goes negative
                    in_progress.pop(0)
                else:
                    c = data[current[0]][current[1]]
                    # Move the beam and change beam location/direction according to character in cell
                    # Remove the beam from in_progress if starts to loop (been on the location with that direction)
                    match c:
                        case '.':
                            new = add_visited(current,dir)
                            if new:
                                not_splitter(current,dir)
                            else:
                                in_progress.pop(0)
                        case '/':
                            new = add_visited(current,dir)
                            if new:
                                match dir:
                                    case [0,1]:
                                        not_splitter(current,[-1,0])
                                    case [1,0]:
                                        not_splitter(current,[0,-1])
                                    case [0,-1]:
                                        not_splitter(current,[1,0])
                                    case [-1,0]:
                                        not_splitter(current,[0,1])
                            else:
                                in_progress.pop(0)
                        case '\\':
                            new = add_visited(current,dir)
                            if new:
                                match dir:
                                    case [0,1]:
                                        not_splitter(current,[1,0])
                                    case [1,0]:
                                        not_splitter(current,[0,1])
                                    case [0,-1]:
                                        not_splitter(current,[-1,0])
                                    case [-1,0]:
                                        not_splitter(current,[0,-1])
                            else:
                                in_progress.pop(0)
                        case '-':
                            new = add_visited(current,dir)
                            if new:
                                match dir:
                                    case [0,1] | [0,-1]:
                                        not_splitter(current,dir)
                                    case [1,0] | [-1,0]:
                                        splitter(current,[0,1],[0,-1])
                            else:
                                in_progress.pop(0)
                        case '|':
                            new = add_visited(current,dir)
                            if new:
                                match dir:
                                    case [1,0] | [-1,0]:
                                        not_splitter(current,dir)
                                    case [0,1] | [0,-1]:
                                        splitter(current,[1,0],[-1,0])
                            else:
                                in_progress.pop(0)
            except: # Index over length
                in_progress.pop(0)

        for line in visited:
            for cell in line:
                if cell:
                    energized += 1

        if not silver_answer:
            silver = energized
            silver_answer = True
        
        if energized > gold:
            gold = energized

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()