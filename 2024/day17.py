def main():
    with open("input17.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    registers = data[0].splitlines()
    a = int(registers[0].split(':')[1])
    b = int(registers[1].split(':')[1])
    c = int(registers[2].split(':')[1])

    program = [ int(x) for x in data[1].split(': ')[1].split(',') ]
    str_program = ",".join([str(x) for x in program])

    def combo_op(x):
        match x:
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                return x
    # up till 240 000 000
    for i in range(780000000,820000000):
        if i % 1000 == 0:
            print(i)
        a = i
        outputs = ""
        pointer = 0
        while True:

            if str_program.startswith(outputs):

                if pointer > len(program)-1:
                    break

                opcode = program[pointer]
                operand = program[pointer+1]

                match opcode:
                    case 0:
                        a = a//(2**combo_op(operand))
                        pointer += 2
                    case 1:
                        b = b ^ operand
                        pointer += 2
                    case 2:
                        b = combo_op(operand) % 8
                        pointer += 2
                    case 3:
                        if a == 0:
                            pointer += 2
                        else:
                            pointer = 0
                    case 4:
                        b = b ^ c
                        pointer += 2
                    case 5:
                        if outputs == "":
                            outputs += str(combo_op(operand) % 8)
                        else:
                            outputs += ','+str(combo_op(operand) % 8)
                        pointer += 2
                    case 6:
                        b = a//(2**combo_op(operand))
                        pointer += 2
                    case 7:
                        c = a//(2**combo_op(operand))
                        pointer += 2
            else:
                break
        #print(outputs)
        if str_program == outputs:
            gold = i
            break


    #outputs = [str(x) for x in outputs]
    #silver = ",".join(outputs)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()