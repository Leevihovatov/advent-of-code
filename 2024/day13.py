def main():
    with open("input13.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    for d in data:
        machine = d.splitlines()
        a = machine[0].replace('+',' ').replace(',','').split()
        a = [int(a[3]), int(a[5])]
        b = machine[1].replace('+',' ').replace(',','').split()
        b = [int(b[3]), int(b[5])]
        prize = machine[2].replace('=',' ').replace(',','').split()
        prize = [int(prize[2]), int(prize[4])]

        wins = []
        for i in range(101):
            for j in range(101):
                if [i*a[0]+j*b[0],i*a[1]+j*b[1]] == prize:
                    wins.append(3*i+j)
                elif i*a[0]+j*b[0] > prize[0] or i*a[1]+j*b[1] > prize[1]:
                    break

        if len(wins) > 0:
            silver += min(wins)


    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()