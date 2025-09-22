def main():
    with open("input11.txt", "r") as f:
        data = f.read().split()

    stones = [int(x) for x in data]
    
    silver = 0
    gold = 0

    for i in range(25):
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif len(str(s)) % 2 == 0:
                new_stones.append(int(str(s)[:int(len(str(s))/2)]))
                new_stones.append(int(str(s)[int(len(str(s))/2):]))
            else:
                new_stones.append(s*2024)

        stones = new_stones
        #print(f'{i} {len(stones)} {stones}')

    silver = len(stones)
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()