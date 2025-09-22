def main():
    with open("input01.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    left_list = []
    right_list = []
    for row in data:
        left_list.append(int(row.split()[0]))
        right_list.append(int(row.split()[1]))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        silver += abs(left_list[i]-right_list[i])
    
    counts = {}
    for i in right_list:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

    for i in left_list:
        try:
            gold += i*counts[i]
        except:
            continue

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()