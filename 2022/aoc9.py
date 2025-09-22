import numpy as np

def main():
    data = open("input9.txt","r",encoding="utf-8").read()
    lines = data.splitlines()
    locs = np.zeros((1000,1000)) #Visited locations
    h = []
    t = [[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500]]
    dh = np.matrix([[2, 1, 2],[1, 0, 1],[2, 1, 2]]) # x+y Distance from head
    st = np.zeros((3,3)) # x+y Steps it would take

    for x in lines:
        d = x.split()[0]
        m = x.split()[1]
        
        #("---")
        #print(h)
        #print(t)

        for i in range(0,int(m)):
            #print(t)

            if d == "R":
                t[0][1] += 1
            if d == "L":
                t[0][1] -= 1
            if d == "D":
                t[0][0] += 1
            if d == "U":
                t[0][0] -= 1

            #print(t[0])

            for k in range(1,10):
                h = [t[k-1][0],t[k-1][1]]
                tx = [t[k][0],t[k][1]]

                if abs(h[0]-tx[0]) > 1 or abs(h[1]-tx[1]) > 1:
                    for r in range(-1,2):
                        for c in range(-1,2):
                            st[r+1][c+1] = abs((h[0]+r)-tx[0]) + abs((h[1]+c)-tx[1])

                    c1 = [0,0]
                    c2 = [0,0]
                    #print(st)
                    for r in range(0,3):
                        for c in range(0,3):
                            rr = r-1
                            rc = c-1
                            if (abs(tx[0]+rr-h[0]) < 2) or (abs(tx[1]+rc-h[1]) < 2):
                                if (st[r][c] == 1) and (dh.item((r,c)) == 1):
                                    c1 = [h[0]+rr,h[1]+rc]
                                if (st[r][c] == 2) and (dh.item((r,c)) == 1):
                                    c2 = [h[0]+rr,h[1]+rc]
                            else:
                                if (st[r][c] == 2) and (dh.item((r,c)) == 2):
                                    c2 = [h[0]+rr,h[1]+rc]
                    #print("c")
                    #print(c1)
                    #print(c2)
                    #("---")
                    if sum(c1) == 0:
                        t[k] = c2
                    else:
                        t[k] = c1
                else:
                    #print("ei")
                    pass

            locs[t[-1][0]][t[-1][1]] = 1
            #print(t[1])

    visited = np.sum(locs)
    print(locs)
    print(visited)

main()
        