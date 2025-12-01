def main():
    with open("input08.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    visited = []
    i = 0
    value = 0
    while i not in visited:

        visited.append(i)

        operation = data[i].split()[0]
        argument = int(data[i].split()[1])

        if operation == 'acc':
            value += argument
            i += 1
        elif operation == 'jmp':
            i += argument
        elif operation == 'nop':
            i += 1

    silver = value

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()