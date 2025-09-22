import numpy as np

def main():
    data = open("input12.txt","r",encoding="utf-8").read()
    map = data.splitlines()

    stepMatrix = np.zeros((len(map),len(map[0])))
    row = 0
    col = 0

    for r in map:
        for c in r:
            if c == "S":
                start = [row, col]
                startRow = row
            if c == "E":
                end = [row, col]
            col += 1
        col = 0
        row += 1

    map[startRow] = map[startRow].replace("S","`")

    current = [end]
    old = []
    next = []
    steps = 0

    while 1 > 0:
        steps += 1
        numCur = 0
        # Neighbouring cells
        for curr in current:
            # try-catch
            next.append([])
            
            next[numCur].append([curr[0],curr[1]+1])
            next[numCur].append([curr[0]+1,curr[1]])
            # To avoid -1 index
            if (curr[1]) != 0:
                next[numCur].append([curr[0],curr[1]-1])         
            if (curr[0]) != 0:
                next[numCur].append([curr[0]-1,curr[1]])
            numCur += 1
        numCur = 0

        old = list(current)
        current.clear()

        for n in next:
            for nn in n:
                # Check if can go
                # try-except for edges
                try:
                    if ord(map[nn[0]][nn[1]]) - ord(map[old[numCur][0]][old[numCur][1]]) >= -1:
                        # Check if already visited
                        if stepMatrix[nn[0]][nn[1]] == 0:
                            current.append([nn[0],nn[1]])
                            stepMatrix[nn[0]][nn[1]] = steps
                except IndexError:
                    pass
            numCur += 1
        next.clear()

        if stepMatrix[start[0]][start[1]] != 0:
            break
        
        # Remove duplicates
        current2 = []
        for i in current:
            if i in current2:
                continue
            else:
                current2.append(i)
        current = list(current2)

        print(current)
        
        numCur = 0
        old.clear()
    
    print(stepMatrix)
    print(stepMatrix[start[0]][start[1]])
main()