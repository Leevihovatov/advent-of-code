import re

def main():
    with open("input04.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    def transpose(data): # For using count_horizontal on transposed data to get up-down down-up texts
        transposed = []
        for i in range(len(data[0])):
            line = "".join([c[i] for c in data])
            transposed.append(line)
        return transposed

    def count_horizontal_xmas(data): # Both normal and reverse
        pattern = 'XMAS'
        count = 0
        for line in data:
            count += len(re.findall(pattern, line)) + len(re.findall(pattern, line[::-1]))
        return count

    transposed_data = transpose(data)

    # Shift the data by one column every row, then later transpose
    # to find the diagonal matches just from horizontal string
    pos_shifted_data = []
    neg_shifted_data = []
    for i,l in enumerate(data):
        pos_shifted_data.append("".join(['.']*i+l.split()+['.']*(len(data)-i-1)))
        neg_shifted_data.append("".join(['.']*(len(data)-i-1)+l.split()+['.']*i))

    silver += count_horizontal_xmas(data)
    silver += count_horizontal_xmas(transposed_data)
    silver += count_horizontal_xmas(transpose(pos_shifted_data))
    silver += count_horizontal_xmas(transpose(neg_shifted_data))

    # Find indexes of A in MAS from both ways shifted (then transposed) data
    # If same index found from both, then MAS crosses that A in both diagonal directions

    def get_mas_index(data):
        pattern = 'MAS'
        positions = []
        dots_above = [0]*len(data[0]) # Used for getting the amount of shift per column to get right original row index

        for i,line in enumerate(data):
            for j, char in enumerate(line):
                if char == '.':
                    dots_above[j] += 1
            
            forward = [[m.start(0)+1, i-dots_above[m.start(0)+1]] for m in re.finditer(pattern, line)]
            reverse = [[len(line)-(m.start(0)+1)-1, i-dots_above[len(line)-(m.start(0)+1)-1]] for m in re.finditer(pattern, line[::-1])]

            positions += forward + reverse
        return positions
    
    a = get_mas_index(transpose(pos_shifted_data))
    b = get_mas_index(transpose(neg_shifted_data))

    for n in a:
        if n in b:
            gold += 1

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()