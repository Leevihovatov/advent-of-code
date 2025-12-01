def main():
    with open("input01.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    rotations = [int(d[1:]) if d[0] == 'R' else -int(d[1:]) for d in data]

    pos = 50

    for r in rotations:

        if r < 0:
            for i in range(1, abs(r)+1):
                pos -= 1
                if pos % 100 == 0:
                    gold += 1
        else:
            for i in range(1, r+1):
                pos += 1
                if pos % 100 == 0:
                    gold += 1


        if pos % 100 == 0:
            silver += 1

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()