def main():
    with open("input04.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    copies_of_cards = [1]*len(data)
    
    for line in data:
        # Split the line into arrays of winning number and own numbers
        # and take the intersection of those to get the matching numbers
        line = line.split()
        divider = line.index('|')
        winning_numbers = line[2:divider]
        elf_numbers = line[divider+1:]
        intersection = list(set(winning_numbers) & set(elf_numbers))
        
        current_game = int(line[1].strip(':'))

        points = 0
        if len(intersection) > 0:
            points = 2**(len(intersection))/2
            silver += points
            
            # Add copies to the next cards by the amount of the current cards 
            for i in range(len(intersection)):
                copies_of_cards[current_game + i] += copies_of_cards[current_game-1]
        
    gold = sum(copies_of_cards)
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()