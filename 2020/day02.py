def main():
    with open("input02.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    for d in data:
        limits = [int(x) for x in d.split()[0].split('-')]
        letter = d.split()[1].replace(':','')
        pwd = d.split()[2]

        n = len(pwd) - len(pwd.replace(letter, ''))

        if n >= limits[0] and n <= limits[1]:
            silver += 1

        letters = pwd[limits[0]-1] + pwd[limits[1]-1]
        if len(letters.replace(letter,'')) == 1:
            gold += 1
        

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()