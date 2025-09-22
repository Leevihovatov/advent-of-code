def main():
    with open("input09.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    for line in data:
        history = []
        history.append([ int(x) for x in line.split()])
        # Calculate the difference layers for the history
        while history[-1].count(0) != len(history[-1]):
            dif = []
            for n in range(len(history[-1])-1):
                dif.append(history[-1][n+1]-history[-1][n])
            history.append(dif)
        
        silver += sum(x[-1] for x in history)

        new_history = 0
        for i in range(-2,-len(history)-1,-1):
            new_history = history[i][0]-new_history
        gold += new_history
        



    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()