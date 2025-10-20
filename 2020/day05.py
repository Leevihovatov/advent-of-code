def main():
    with open("input05.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    max_row = 127
    max_col = 7

    powers = [2**n for n in range(6)]
    powers.reverse()

    c_powers = [2, 1]

    seats = []

    for d in data:
        rows = d[:7]
        columns = d[7:]

        r = 64
        c = 4

        for i,x in enumerate(rows):
            if i == 6:
                if x == 'F':
                    r -= 1
            else:
                if x == 'F':
                    r -= powers[i]
                if x == 'B':
                    r += powers[i]

        for i,x in enumerate(columns):
            if i == 2:
                if x == 'L':
                    c -= 1
            else:
                if x == 'L':
                    c -= c_powers[i]
                if x == 'R':
                    c += c_powers[i]

        if r * 8 + c > silver:
            silver = r * 8 + c

        seats.append([r,c])

    first_row = min([s[0] for s in seats])
    first_row_seats = [s[1] for s in seats if s[0] == first_row]
    first_column = min(first_row_seats)

    last_row = max([s[0] for s in seats])
    last_row_seats = [s[1] for s in seats if s[0] == last_row]
    last_column = max(last_row_seats)


    for r in range(first_row, last_row+1):
        if r == first_row:
            for c in range(first_column,max_col+1):
                if [r,c] not in seats:
                    gold = r * 8 + c
        elif r == last_row:
            for c in range(0,last_column+1):
                if [r,c] not in seats:
                    gold = r * 8 + c
        else:
            for c in range(max_col+1):
                if [r,c] not in seats:
                    gold = r * 8 + c

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()