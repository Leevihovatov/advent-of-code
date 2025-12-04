def main():
    with open("input03.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0
    
    g_joltage_length = 12

    for d in data:
        batteries = list(d)

        # Silver search
        b1 = batteries[:-1]

        first_ind = b1.index(max(b1))
        first = b1[first_ind]

        b2 = batteries[first_ind + 1:]
        second_ind = b2.index(max(b2))
        second = b2[second_ind]

        silver += int(first + second)

        # Gold search
        gold_joltage = ''
        front_ind = 0
        
        for i in range(g_joltage_length - 1, 0, -1):
            b = batteries[front_ind:-i]

            gold_joltage += max(b)
            front_ind += b.index(max(b)) + 1
        
        b = batteries[front_ind:]
        gold_joltage += max(b)

        gold += int(gold_joltage)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()