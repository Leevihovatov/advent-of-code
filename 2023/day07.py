def main():
    with open("input07.txt", "r") as f:
        data = f.read().splitlines()
    
    total = 0
    mode = 'gold'
    
    hands = []
    bids = []
    combos = []
    
    for line in data:
        fixed_hand = []
        hand = list(line.split()[0])
        # Changing the letters to values for comparing them
        for card in hand:
            if mode == 'gold':
                new_card = card.replace('A','14').replace('K','13').replace('Q','12').replace('J','1').replace('T','10')
            else:
                new_card = card.replace('A','14').replace('K','13').replace('Q','12').replace('J','11').replace('T','10')
            fixed_hand.append(int(new_card))
        hands.append(fixed_hand)
        checked = []
        current_combo = ''
        jokers = 0
        # Checking the current combination of the hand
        # Five of a kind - High card
        for card in fixed_hand:  
            if current_combo in ['5','4','23','32','22']:
                break
            if card == 1:
                pass
            else:
                if card not in checked:
                    count = fixed_hand.count(card)
                    if count != 1:
                        current_combo += str(count)
                        checked.append(card)
        jokers = fixed_hand.count(1)
        # Creating a combination rank for each poker combination
        # and giving them ranks 0-6
        if jokers > 0:
            match current_combo:
                case '5':
                    combos.append(6)
                case '4':
                    combos.append(6)
                case x if x in ['23','32']:
                    combos.append(4)
                case '3':
                    if jokers == 1:
                        combos.append(5)
                    else:
                        combos.append(6)
                case '22':
                    combos.append(4)
                case '2':
                    match jokers:
                        case 1:
                            combos.append(3)
                        case 2:
                            combos.append(5)
                        case 3:
                            combos.append(6)
                case '':
                    match jokers:
                        case 1:
                            combos.append(1)
                        case 2:
                            combos.append(3)
                        case 3:
                            combos.append(5)
                        case 4:
                             combos.append(6)
                        case 5:
                            combos.append(6)  
        else:
            match current_combo:
                case '5':
                    combos.append(6)
                case '4':
                    combos.append(5)
                case x if x in ['23','32']:
                    combos.append(4)
                case '3':
                    combos.append(3)
                case '22':
                    combos.append(2)
                case '2':
                    combos.append(1)
                case '':
                    combos.append(0)
        bids.append(int(line.split()[1]))
    ranked_hands = []
    ranked_bids = []
    ranked_combos = [] # Poker hand combination ranks 0-6
    ranked_hands.append(hands[0])
    ranked_combos.append(combos[0])
    ranked_bids.append(bids[0])
    # This loop ranks the hands like wanted in the task
    for i in range(1,len(hands)):          
        try:
            ind = ranked_combos.index(combos[i])
            found = True
        except:
            found = False
        if not found: # If not that poker hand rank yet in the ranked hands
            for j in [-1,1,-2,2,-3,3,-4,4,-5,5,-6,6]:
                try:
                    ind = ranked_combos.index(combos[i]+j)
                    count = ranked_combos.count(ranked_combos[ind])
                    found = True
                    break
                except:
                    pass
            if j<0:
                ranked_combos.insert(ind+count,combos[i])
                ranked_hands.insert(ind+count,hands[i])
                ranked_bids.insert(ind+count,bids[i])
            else:
                ranked_combos.insert(ind,combos[i])
                ranked_hands.insert(ind,hands[i])
                ranked_bids.insert(ind,bids[i])
        else:
            found = False
            # Finding how many same poker hand rank hands are there ranked so far
            # Comparing the hands card by card to find correct place for hand
            count = ranked_combos.count(combos[i])
            if count > 1:
                for m in range(ind,ind+count):                   
                    for c in range(5):
                        dif = hands[i][c] - ranked_hands[m][c]
                        if dif == 0:
                            continue
                        elif dif < 0:
                            found = True
                            ranked_combos.insert(m,combos[i])
                            ranked_hands.insert(m,hands[i])
                            ranked_bids.insert(m,bids[i])
                        else:
                            break
                        if found:
                            break
                    if found:
                        break
                if not found:
                    ranked_combos.insert(m+1,combos[i])
                    ranked_hands.insert(m+1,hands[i])
                    ranked_bids.insert(m+1,bids[i])
            else:
                for c in range(5):
                    dif = hands[i][c] - ranked_hands[ind][c]
                    if dif == 0:
                        continue
                    elif dif < 0:
                        found = True
                        ranked_combos.insert(ind,combos[i])
                        ranked_hands.insert(ind,hands[i])
                        ranked_bids.insert(ind,bids[i])
                    else:
                        found = True
                        ranked_combos.insert(ind+1,combos[i])
                        ranked_hands.insert(ind+1,hands[i])
                        ranked_bids.insert(ind+1,bids[i])
                    if found:
                        break
    
    for i in range(len(ranked_bids)):
        total += (i+1)*ranked_bids[i]
                    
    print(f'Total: {total}')

if __name__ == "__main__":
    main()