def main():
    with open("input01.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0
    
    numbers = ['one','two','three','four','five','six','seven','eight','nine']
    for line in data:        

        # Finding the first digit
        for i in range(len(line)):
            if line[i].isnumeric():
                first = line[i]
                break
            
        # Finding the last digit
        for i in range(1,len(line)+1):
            if line[-i].isnumeric():
                last = line[-i]
                break
        
        number = int(first+last)
        silver += number
        
        ## Gold star
        # Creating a new line with only numbers by concatenating
        # numbers to new line as they come up in the original line 
        fixed_line = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                fixed_line += line[i]
            else:
                # Checking if the line start with any written number at the current index
                for n in range(len(numbers)):
                    try:
                        if (line[i:].startswith(numbers[n])):
                            fixed_line += str(n+1)
                            break
                    except:
                        pass
        number = int(fixed_line[0]+fixed_line[-1])
        gold += number
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()