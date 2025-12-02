def main():
    with open("input02.txt", "r") as f:
        data = f.read().split(',')
    
    silver = 0
    gold = 0

    for d in data:
        for i in range(int(d.split('-')[0]), int(d.split('-')[1]) + 1):
            x = str(i)
            l = len(x)

            if l % 2 == 0:
                if x[:int(l/2)] == x[int(l/2):]:
                    silver += i

            for k in range(1, int(l/2)+1):
                pattern = x[:k]
                if x.replace(pattern, '') == '':
                    gold += i
                    break

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()