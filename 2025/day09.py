# Spent a lot of time debugging my linear equation calculations
# This is what you get for not wanting to use ready made packages for that kind of math

def main():
    with open("input09.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    coords = [[int(d.split(',')[0]), int(d.split(',')[1])] for d in data]
    lines = []

    for i,c in enumerate(coords):
        prev = coords[i-1]
        lines.append([prev, c])

    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            area = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
            if area > silver:
                silver = area

    def get_eq(points):
        a = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
        b = points[0][1] - ((points[1][1]-points[0][1])/(points[1][0]-points[0][0]))*points[0][0]

        return a, b

    # Go through corner pairs
    # Take the equations for the two diagonal passing through the rectangle corners
    # If the diagonals intersect with any of the border lines of the big area (between the corners points of the diagonal)
    # the rectangle is not completely within the big shape

    for i in range(len(coords)-1):
        if i % 100 == 0: print(i)
        for j in range(i+1, len(coords)):
            if coords[i][0] == coords[j][0] or coords[i][1] == coords[j][1]:
                pass
            else:
                area = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
                
                if area > gold:
                    corners1 = sorted([coords[i], coords[j]], key=lambda x: x[0])
                    corners2 = sorted([[coords[i][0], coords[j][1]], [coords[j][0], coords[i][1]]], key=lambda x: x[0])

                    a1, b1 = get_eq(corners1)
                    a2, b2 = get_eq(corners2)

                    intersect = False
                    for l in lines:
                        xs = sorted([l[0][0], l[1][0]])
                        ys = sorted([l[0][1], l[1][1]])
                        if (len(set([corners1[0][0], xs[0], xs[1]])) == 1 or len(set([corners2[0][0], xs[0], xs[1]])) == 1 or
                            len(set([corners1[1][0], xs[0], xs[1]])) == 1 or len(set([corners2[1][0], xs[0], xs[1]])) == 1 or
                            len(set([corners1[0][1], ys[0], ys[1]])) == 1 or len(set([corners2[0][1], ys[0], ys[1]])) == 1 or
                            len(set([corners1[1][1], ys[0], ys[1]])) == 1 or len(set([corners2[1][1], ys[0], ys[1]])) == 1):
                            pass
                        else:
                            if l[0][0] == l[1][0]: # Vertical line, look for y between
                                y1 = a1*l[0][0] + b1
                                y2 = a2*l[0][0] + b2
                                
                                if ((y1 >= ys[0] and y1 <= ys[1]) or (y2 >= ys[0] and y2 <= ys[1])) and (xs[0] >= corners1[0][0] and xs[0] <= corners1[1][0]):
                                    intersect = True
                                    break
                            if l[0][1] == l[1][1]: # Horizontal line, look for x between
                                x1 = (l[0][1]-b1)/a1
                                x2 = (l[0][1]-b2)/a2
                                
                                if ((x1 >= xs[0] and x1 <= xs[1]) or (x2 >= xs[0] and x2 <= xs[1])) and (ys[0] >= min([corners1[0][1],corners1[1][1]]) and ys[0] <= max([corners1[0][1],corners1[1][1]])):
                                    intersect = True
                                    break

                    if not intersect:
                        gold = area

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()