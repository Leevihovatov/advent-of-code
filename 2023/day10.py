# Welcome to the matchcaseifelse-jungle
def main():
    with open("input10.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    # Create . padding around the data to help
    # when checking the edges
    for i in range(len(data)):
        data[i] = '.'+data[i]+'.'        
    padding = "."*len(data[0])
    data.insert(0,padding)
    data.append(padding)

    data = [list(x) for x in data]

    # Change the pipes that can't be in a loop (don't have 2 pipes correctly attaching to them) to dots
    # First thought I could the silver result from here: Remaining pipes/2 but there are also separate pipe loops
    # This is now done as preparation for the second part of the task
    # Also the second part code wouldn't work if there are other pipe loops inside the S-pipe loop
    noneed = 1
    while noneed != 0:
        noneed = 0
        for i in range(1,len(data)-1):
            for j in range(1,len(data[0])-1):
                current = data[i][j]
                if current == '.':
                    pass
                elif current == 'S':
                    start = [i,j]
                else:
                    # Check if there are invalid pipe connections
                    match current:
                        case '|':
                            if data[i-1][j] not in ['F','7','|','S'] or data[i+1][j] not in ['J','L','|','S']:
                                noneed += 1
                                data[i][j] = '.'
                        case '-':
                            if data[i][j-1] not in ['F','L','-','S'] or data[i][j+1] not in ['J','7','-','S']:
                                noneed += 1
                                data[i][j] = '.'
                        case 'F':
                            if data[i+1][j] not in ['J','L','|','S'] or data[i][j+1] not in ['J','7','-','S']:
                                noneed += 1
                                data[i][j] = '.'
                        case '7':
                            if data[i][j-1] not in ['F','L','-','S'] or data[i+1][j] not in ['J','L','|','S']:
                                noneed += 1
                                data[i][j] = '.'
                        case 'J':
                            if data[i-1][j] not in ['F','7','|','S'] or data[i][j-1] not in ['F','L','-','S']:
                                noneed += 1
                                data[i][j] = '.'
                        case 'L':
                            if data[i-1][j] not in ['F','7','|','S'] or data[i][j+1] not in ['J','7','-','S']:
                                noneed += 1
                                data[i][j] = '.'

    only_loops = []
    for line in data:
            only_loops.append(''.join(line))

    visited = []
    visited.append(start)
    inside = []
    new_pipe = True
    # Start from S and go through the pipes until we loop back to S
    # Silver result is the amount of visited pipes divided by two as the furthest point is halfway the whole loop
    while new_pipe:
        new_pipe = False
        pipe_type = only_loops[start[0]][start[1]]
        i = start[0]
        j = start[1]
        # Well, here it checks the possible connections to move to next pipe through the loop, not nice code
        # For the gold part this saves the left hand side of the pipe as inside-the-loop index
        # For a loop the other side is always inside, had to check before whether it is righ or left side
        # for my way of going around the loop
        match pipe_type:
            case 'S':
                if only_loops[start[0]][start[1]+1] in ['7','J','-']:
                    that_pipe = [start[0],start[1]+1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        start = that_pipe
                        new_pipe = True
                if only_loops[start[0]+1][start[1]] in ['L','J','|'] and not new_pipe:
                    that_pipe = [start[0]+1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        start = that_pipe
                        new_pipe = True
                if only_loops[start[0]][start[1-1]] in ['L','F','-'] and not new_pipe:
                    that_pipe = [start[0],start[1]-1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        start = that_pipe
                        new_pipe = True
                if only_loops[start[0]-1][start[1]] in ['F','7','|'] and not new_pipe:
                    that_pipe = [start[0]-1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        start = that_pipe
                        new_pipe = True
            case '|':
                if only_loops[i-1][j] in ['F','7','|','S']:
                    that_pipe = [start[0]-1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i,j-1])
                        start = that_pipe
                        new_pipe = True
                if only_loops[i+1][j] in ['J','L','|','S'] and not new_pipe:
                    that_pipe = [start[0]+1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i,j+1])
                        start = that_pipe
                        new_pipe = True                    
            case '-':
                if only_loops[i][j-1] in ['F','L','-','S']:
                    that_pipe = [start[0],start[1]-1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i+1,j])
                        start = that_pipe
                        new_pipe = True
                if only_loops[i][j+1] in ['J','7','-','S'] and not new_pipe:
                    that_pipe = [start[0],start[1]+1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i-1,j])
                        start = that_pipe
                        new_pipe = True                    
            case 'F':
                if only_loops[i+1][j] in ['J','L','|','S']:
                    that_pipe = [start[0]+1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i,j+1])
                        start = that_pipe
                        new_pipe = True
                if only_loops[i][j+1] in ['J','7','-','S'] and not new_pipe:
                    that_pipe = [start[0],start[1]+1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i-1,j])
                        inside.append([i,j-1])
                        start = that_pipe
                        new_pipe = True                    
            case '7':
                if only_loops[i][j-1] in ['F','L','-','S']:
                    that_pipe = [start[0],start[1]-1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i+1,j])
                        start = that_pipe
                        new_pipe = True
                if only_loops[i+1][j] in ['J','L','|','S'] and not new_pipe:
                    that_pipe = [start[0]+1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i,j+1])
                        inside.append([i-1,j])
                        start = that_pipe
                        new_pipe = True                    
            case 'J':
                if only_loops[i-1][j] in ['F','7','|','S']:
                    that_pipe = [start[0]-1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i,j-1])
                        start = that_pipe
                        new_pipe = True
                if only_loops[i][j-1] in ['F','L','-','S'] and not new_pipe:
                    that_pipe = [start[0],start[1]-1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i+1,j])
                        inside.append([i,j+1])
                        start = that_pipe
                        new_pipe = True                   
            case 'L':
                if only_loops[i-1][j] in ['F','7','|','S']:
                    that_pipe = [start[0]-1,start[1]]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i,j-1])
                        inside.append([i-1,j])
                        start = that_pipe
                        new_pipe = True
                if only_loops[i][j+1] in ['J','7','-','S'] and not new_pipe:
                    that_pipe = [start[0],start[1]+1]
                    if that_pipe not in visited:
                        visited.append(that_pipe)
                        inside.append([i-1,j])
                        start = that_pipe
                        new_pipe = True

    silver = len(visited)/2

    inside = set(tuple(row) for row in inside)
    inside_dots = []

    # Take only the . values from the inside-the-loop indexes as there the pipe can go side-to-side with itself
    for n in inside:
        if only_loops[n[0]][n[1]] == '.':
            inside_dots.append([n[0],n[1]])

    # Check if there are bigger areas of dots inside the loop as the earlier loop only takes the dots
    # that are right next to pipe
    for id in inside_dots:
        more = True
        r = id[0]
        c = id[1]
        while more:
            more = False
            if only_loops[r][c+1] == '.' and [r,c+1] not in inside_dots:
                inside_dots.append([r,c+1])
                c += 1
                more = True
    
    gold = len(inside_dots)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()