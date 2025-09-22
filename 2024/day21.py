def main():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    numpad_pos = { #[x,y]
        '1': [1,0],
        '2': [1,1],
        '3': [1,2],
        '4': [2,0],
        '5': [2,1],
        '6': [2,2],
        '7': [3,0],
        '8': [3,1],
        '9': [3,2],
        '0': [0,1],
        'A': [0,2]
    }

    directional_pos = { #[x,y]
        '<': [0,0],
        'v': [0,1],
        '>': [0,2],
        '^': [1,1],
        'A': [1,2]
    }

    def get_numpad_dirs(move): # Right, up, left, down to avoid empty
        dirs = ""
        if move[1] > 0:
            dirs += move[1]*'>'
        if move[0] > 0:
            dirs += move[0]*'^'
        if move[1] < 0:
            dirs += abs(move[1])*'<'
        if move[0] < 0:
            dirs += abs(move[0])*'v'
        
        return dirs
    
    def get_directional_dirs(move): # Right, up, down, left to avoid empty
        dirs = ""
        if move[0] < 0:
            dirs += abs(move[0])*'v'
        
        if move[1] > 0:
            dirs += move[1]*'>'
        if move[0] > 0:
            dirs += move[0]*'^'
        
        if move[1] < 0:
            dirs += abs(move[1])*'<'
        return dirs

    def get_robot_moves(move):
        match move:
            case 'A<':
                return 'v<<'
            case 'A>':
                return 'v'
            case 'Av':
                return 'v<'
            case 'A^':
                return '<'
            case '<>':
                return '>>'
            case '<^':
                return '>^'
            case '<v':
                return '>'
            case '<A':
                return '>>^'
            case '><':
                return '<<'
            case '>v':
                return '<'
            case '>^':
                return '^<'
            case '>A':
                return '^'
            case 'v>':
                return '>'
            case 'v^':
                return '^'
            case 'v<':
                return '<'
            case 'vA':
                return '>^'
            case '^>':
                return 'v>'
            case '^v':
                return 'v'
            case '^<':
                return 'v<'
            case '^A':
                return '>'
            case _:
                return ''

    full = []
    for d in data:
        code = 'A'+d

        instructions = ""
        for i in range(len(code)-1):
            move = [
                numpad_pos[code[i+1]][0] - numpad_pos[code[i]][0],
                numpad_pos[code[i+1]][1] - numpad_pos[code[i]][1]
            ]
            #print(f'{code[i]} -> {code[i+1]}: {move}')
            if code[i:i+2] == '37':
                instructions += '<<^^A'
            elif code[i:i+2] in ['34','67']:
                instructions += '<<^A'
            elif code[i:i+2] == 'A5':
                instructions += '<^^A'
            elif code[i:i+2] == '86':
                instructions += 'v>A'
            else:
                dirs = get_numpad_dirs(move)
                instructions += dirs + 'A'

        print(instructions)


        for i in range(25):
            code = 'A'+instructions
            instructions = ""
            for j in range(len(code)-1):
                #print(code[i:i+2])
                instructions += get_robot_moves(code[j:j+2])+'A'
                """ move = [
                    directional_pos[code[i+1]][0] - directional_pos[code[i]][0],
                    directional_pos[code[i+1]][1] - directional_pos[code[i]][1]
                ]
                #print(f'{code[i]} -> {code[i+1]}: {move}')
                dirs = get_directional_dirs(move)
                instructions += dirs + 'A' """
            print(f'{i}: {len(instructions)}')

            

        """ print(instructions)

        code = 'A'+instructions
        instructions = ""
        for i in range(len(code)-1):
            move = [
                directional_pos[code[i+1]][0] - directional_pos[code[i]][0],
                directional_pos[code[i+1]][1] - directional_pos[code[i]][1]
            ]
            #print(f'{code[i]} -> {code[i+1]}: {move}')
            dirs = get_directional_dirs(move)
            instructions += dirs + 'A' """ 

        full.append(len(instructions)*int(d[:-1]))
    
    print(instructions)
    print(sum(full))

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()