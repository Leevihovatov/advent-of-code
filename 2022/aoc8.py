import numpy as np

def main():
    data = open("input8.txt","r",encoding="utf-8").read()
    lines = data.splitlines()
    forest = []
    for l in lines:
        trees = []
        for x in str(l):
            trees.append(x)
        forest.append(trees)

    vis = np.zeros((len(lines), len(lines[0])))
    sP = np.ones((len(lines), len(lines[0])))

    fr = 0
    fl = 0
    fu = 0
    fd = 0
    for r in range(1,len(lines)-1):
        fl = int(forest[r][0])
        for c in range(1,len(lines[0])-1):
            
            tree = int(forest[r][c])
            
            if tree > fl:
                vis[r][c] = 1
                fl = tree             

    for c in range(1,len(lines[0])-1):
        fu = int(forest[0][c])
        for r in range(1,len(lines)-1):
         
            tree = int(forest[r][c])
            
            if tree > fu:
                vis[r][c] = 1
                fu = tree   

    for r in range(1,len(lines)-1):
        fr = int(forest[r][-1])
        for c in range(len(lines[0])-2,0,-1):
            
            tree = int(forest[r][c])
            
            if tree > fr:
                vis[r][c] = 1
                fr = tree             
            
    for c in range(1,len(lines[0])-1):
        fd = int(forest[-1][c])
        for r in range(len(lines)-2,0,-1):

            tree = int(forest[r][c])
           
            if tree > fd:
                vis[r][c] = 1
                fd = tree  

    visibleTrees = np.sum(vis) + 2*len(lines) + 2*len(lines[0]) - 4
    print(visibleTrees)
    print(vis)

    #2

    for r in range(1,len(lines)-1):
        fl = int(forest[r][0])
        for c in range(1,len(lines[0])-1):
            tree = int(forest[r][c])
            s = 1
            for t in range(c+1,len(lines[0])):
                if int(forest[r][t]) >= tree:
                    s = t-c
                    break
                if t == len(lines[0])-1:
                    s = t-c
            sP[r][c] *= s

    for c in range(1,len(lines[0])-1):
        fu = int(forest[0][c])
        for r in range(1,len(lines)-1):
            tree = int(forest[r][c])
            s = 1
            for t in range(r+1,len(lines)):
                if int(forest[t][c]) >= tree:
                    s= t-r
                    break
                if t == len(lines)-1:
                    s = t-r
            sP[r][c] *= s

    for r in range(1,len(lines)-1):
        fr = int(forest[r][-1])
        for c in range(len(lines[0])-2,0,-1):
            tree = int(forest[r][c])
            s = 1
            for t in range(c-1,-1,-1):
                if int(forest[r][t]) >= tree:
                    s = c-t
                    break
                if t == 0:
                    s = c-t
            sP[r][c] *= s

    for c in range(1,len(lines[0])-1):
        fd = int(forest[-1][c])
        for r in range(len(lines)-2,0,-1):
            tree = int(forest[r][c])
            s = 1
            for t in range(r-1,-1,-1):
                if int(forest[t][c]) >= tree:
                    s = r-t
                    break
                if t == 0:
                    s = r-t
            sP[r][c] *= s

    maxScenic = np.amax(sP)
    print(sP)
    print(maxScenic)
main()