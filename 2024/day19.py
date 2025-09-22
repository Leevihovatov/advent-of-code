def main():
    with open("input19.txt", "r") as f:
        data = f.read().splitlines()
    
    towels = data[0].split(', ')
    designs = data[1:]
    del designs[0]

    silver = 0
    gold = 0

    def check_start(design):
        #print(design)
        possible = 0
        if design == "":
            return 1
        else:
            potential = [t for t in towels if t in design]
            for p in potential:
                """ if possible == 1:
                    return 1 """
                if design.startswith(p):
                    #print(p)
                    possible += check_start(design[len(p):])

        return possible

    for d in designs:
        
        n_possible = check_start(d)
        if n_possible != 0:
            silver += 1
        gold += n_possible
        print(d)
        #print(f'{d} : {po}')

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()