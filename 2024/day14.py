def main():
    with open("input14.txt", "r") as f:
        data = f.read().splitlines()

    w = 101
    h = 103

    area = []
    for i in range(h):
        area.append([0]*w)

    silver = 0
    gold = 0

    for d in data:
        d = d.replace('=',',').replace(' ',',').split(',')
        p = [int(d[2]), int(d[1])]
        v = [int(d[5]), int(d[4])]

        oob_pos = [p[0]+100*v[0], p[1]+100*v[1]]

        blocks = [oob_pos[0] // h, oob_pos[1] // w]

        grid_pos = [oob_pos[0]-blocks[0]*h, oob_pos[1]-blocks[1]*w]
        grid_pos = [abs(x) for x in grid_pos]

        area[grid_pos[0]][grid_pos[1]] += 1

    """ for a in area:
        print(a) """

    quadrants = [
        [[0,h//2], [0,w//2]],
        [[0,h//2], [w//2+1,w]],
        [[h//2+1,h], [0,w//2]],
        [[h//2+1,h], [w//2+1,w]]
    ]

    quadrant_sums = []
    for q in quadrants:
        q_sum = 0
        for i in range(q[0][0],q[0][1]):
            q_sum += sum(area[i][q[1][0]:q[1][1]])
        quadrant_sums.append(q_sum)

    silver = quadrant_sums[0]*quadrant_sums[1]*quadrant_sums[2]*quadrant_sums[3]

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()