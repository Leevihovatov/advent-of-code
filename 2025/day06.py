def main():
    with open("input06.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    def calculate(operator, numbers):

        if operator == '+':
            return sum(numbers)
        
        if operator == '*':
            product = 1
            for n in numbers:
                product *= n
            return product

    # Silver
    operators = data[-1].split()
    int_data = []
    for i in range(len(data)-1):
        int_data.append([int(x) for x in data[i].split()])

    for i in range(len(int_data[0])):
        numbers = [d[i] for d in int_data]

        silver += calculate(operators[i], numbers)

    # Gold
    str_list_operators = list(data[-1])
    str_list_data = []
    for i in range(len(data)-1):
        str_list_data.append(list(data[i]))

    diff = len(str_list_data[0]) - len(str_list_operators)
    str_list_operators += [' ']*diff

    rows = len(str_list_data)
    numbers = []
    operator = None
    for i in range(len(str_list_data[0])):
        if str_list_operators[i] != ' ':
            operator = str_list_operators[i]

        number = ''
        for j in range(rows):
            number += str_list_data[j][i]

        number = number.strip()
        if number == '':
            gold += calculate(operator, numbers)
            numbers = []
        else:
            numbers.append(int(number))

    gold += calculate(operator, numbers)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()