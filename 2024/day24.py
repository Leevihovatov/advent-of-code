def main():
    with open("input24.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    bit_data = data[0].splitlines()
    gate_data = data[1].splitlines()

    bits = {}
    for b in bit_data:
        bits[b.split()[0][:-1]] = int(b.split()[1])

    while len(gate_data) > 0:
        for g in gate_data:
            inputs = [g.split()[0], g.split()[2]]
            oper = g.split()[1]
            output = g.split()[4]

            if inputs[0] in bits and inputs[1] in bits:
                if oper == 'AND':
                    bits[output] = bits[inputs[0]] and bits[inputs[1]]
                elif oper == 'OR':
                    bits[output] = bits[inputs[0]] or bits[inputs[1]]
                elif oper == 'XOR':
                    bits[output] = bits[inputs[0]] ^ bits[inputs[1]]
                gate_data.remove(g)

    for b in bits:
        if b.startswith('z'):
            if bits[b] == 1:
                silver += 2 ** int(b[1:])

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()