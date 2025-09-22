import copy

def main():
    with open("input12.txt", "r") as f:
        data = f.read().splitlines()

    calculated = []
    for i, d in enumerate(data):
        data[i] = list(d)
        calculated.append([0]*len(d))
    
    max_row = len(data)-1
    max_col = len(data[0])-1

    silver = 0
    gold = 0

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # For gold, calculating number of sides
    # Check column numbers of same row fences
    # Every time sorted columns are not consecutive numbers
    # Means + 1 different side on that direction
    def check_tp(sides): # For top and bottom fences
        n = 0
        rows = []
        for s in sides:
            if s[0] not in rows:
                rows.append(s[0])

        for r in rows:
            cols = []
            for s in sides:
                if s[0] == r:
                    cols.append(s[1])

            cols.sort()

            if len(cols) == 1:
                n += 1
            else:
                side_breaks = 0
                for c in range(0, len(cols)-1):
                    if cols[c+1]-cols[c] > 1:
                        side_breaks += 1
                n += side_breaks + 1

        return n
    
    def check_lr(sides): # For left and right fences
        n = 0
        cols = []
        for s in sides:
            if s[1] not in cols:
                cols.append(s[1])

        for c in cols:
            rows = []
            for s in sides:
                if s[1] == c:
                    rows.append(s[0])

            rows.sort()

            if len(rows) == 1:
                n += 1
            else:
                side_breaks = 0
                for r in range(0, len(rows)-1):
                    if rows[r+1]-rows[r] > 1:
                        side_breaks += 1
                n += side_breaks + 1

        return n

    # Search cardinal directions for same letter
    # If not same letter in direction: there is fence
    # After all cells in region found, mark them checked so we can skip them later
    for i, d in enumerate(data):
        for j, c in enumerate(d):

            if calculated[i][j] == 0:
                to_be_added = [[i,j]]
                region = []
                fence = 0 # For silver calculations
                sides = {'T': [], 'R': [], 'B': [], 'L': []} # For gold calculation
                region_sides = 0
                while len(to_be_added) > 0:
                    new_ones = []

                    for t in to_be_added:
                        for dir in dirs:
                            new = [t[0]+dir[0], t[1]+dir[1]]
                            if new[0] >= 0 and new[0] <= max_row and new[1] >= 0 and new[1] <= max_col and data[new[0]][new[1]] == c: # Belongs in the same region
                                if [new[0], new[1]] not in region and [new[0], new[1]] not in new_ones:
                                    new_ones.append([new[0], new[1]])
                            else: # Doesn't belong in the same region
                                fence += 1
                                match dir:
                                    case [-1, 0]:
                                        sides['T'].append(t)
                                    case [0, 1]:
                                        sides['R'].append(t)
                                    case [1, 0]:
                                        sides['B'].append(t)
                                    case [0, -1]:
                                        sides['L'].append(t)
                        region.append(t)
                    to_be_added = copy.deepcopy(new_ones)

                # Check number of sides in each direction
                region_sides += check_tp(sides['T'])
                region_sides += check_tp(sides['B'])
                region_sides += check_lr(sides['R'])
                region_sides += check_lr(sides['L'])

                for r in region:
                    calculated[r[0]][r[1]] = 1

                silver += (len(region)*fence)
                gold += (len(region)*region_sides)

            else:
                continue

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()