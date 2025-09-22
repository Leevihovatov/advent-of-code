# Yesterday, all my troubles seemed so far away

import re
def main():
    with open("input03.txt", "r") as f:
        data = f.read().splitlines()
    
    # Create . padding around the data to help
    # when checking the numbers on the edge
    for i in range(len(data)):
        data[i] = '.'+data[i]+'.'
        
    padding = "."*len(data[0])
    data.insert(0,padding)
    data.append(padding)

    silver = 0
    gold = 0

    # Find all the numbers on the line and get their start and end indices
    def find_numbers(line):
        current_number = []
        number_indices = []
        for i in range(len(line)):
            if line[i].isnumeric():
                current_number.append(i)
            elif not line[i].isnumeric() and not current_number:
                continue
            else:
                if len(current_number) == 1: # One digit number
                    number_indices.append(current_number[0])
                else:
                    number_indices.append([current_number[0],current_number[-1]])
                current_number = []
        return number_indices

    # Return only the valid numbers (as numbers, not indices) from all the numbers on the line
    def check_valid_numbers(number_indices, line):
        valid_numbers = []
        regexp = re.compile(r'[*\-#@\+$=/%&]')
        for indices in number_indices:
            # Save all the characters that are in a square around the number
            chars = ''
            for i in range(line-1,line+2):
                try: # Multidigit number
                    for j in range(indices[0]-1,indices[1]+2):
                        chars += data[i][j]
                except: #Single digit number
                    for j in range(indices-1,indices+2):
                        chars += data[i][j]
            # If there are special characters around save the number as a valid number
            if regexp.search(chars):
                try: # Multidigit
                    valid_number = ''
                    for n in range(indices[0],indices[-1]+1):
                        valid_number += data[line][n]
                    valid_numbers.append(int(valid_number))
                except: # Single digit
                    valid_numbers.append(int(data[line][indices]))
        return valid_numbers

    # Returns gear ratios of all valid gears in the line
    def find_gears(line, line_i, number_indices):
        gear_ratios = []
        # Go through characters in line to find gears (*)
        for i in range(0,len(line)):
            surrounding = []
            touching = []
            if line[i] == '*':
                # Save the indices of 3x3 square around the gear
                for r in range(line_i-1,line_i+2):
                    for c in range(i-1,i+2):
                        surrounding.append([r,c])
                # Check if the gear surrounding indices overlap with the indices of the numbers
                # on the three lines on the 3x3 square
                # Lots of for loops and different situation whether the numbers are single or multidigit
                # If there is an overlap, save the overlapping number
                for r in range(line_i-1,line_i+2):
                    if number_indices[r-1]:
                        try: # Multiple numbers
                            for number in number_indices[r-1]:
                                try: # Multidigit
                                    for c in range(number[0],number[1]+1):
                                        if [r,c] in surrounding:
                                            valid_number = ''
                                            for n in range(number[0],number[1]+1):
                                                valid_number += data[r][n]
                                            if int(valid_number) not in touching:
                                                touching.append(int(valid_number))
                                except: # Single digit
                                        if [r,number] in surrounding:
                                            touching.append(int(data[r][number]))
                        except:
                            number = number_indices[r-1]
                            try: # Multidigit
                                for c in range(number[0],number[1]+1):
                                    if [r, c] in surrounding:
                                        valid_number = ''
                                        for n in range(number[0],number[1]+1):
                                            valid_number += data[r][n]
                                        if int(valid_number) not in touching:
                                            touching.append(int(valid_number))
                            except: # Single digit
                                    if [r,number] in surrounding:
                                        touching.append(int(data[r][number]))
            gear_ratio = 0
            # Calculate the gear ratio if there are exactly two numbers touching the gear
            try:
                if len(touching) == 2:
                    gear_ratio = touching[0]*touching[1]
                    gear_ratios.append(gear_ratio)
            except:
                pass
        return gear_ratios

    all_number_indices = []
    for i in range(1,len(data)-1):
        number_indices = find_numbers(data[i])
        all_number_indices.append(number_indices)
        valid_numbers=[]
        if number_indices:
            valid_numbers = check_valid_numbers(number_indices, i)
        silver += sum(valid_numbers)

    # Another loop for the second part
    for i in range(1,len(data)-1): # There are no gears on the first or last line of data, so this happens to work
        gear_ratios = find_gears(data[i], i, all_number_indices)
        gold += sum(gear_ratios)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()