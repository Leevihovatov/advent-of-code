def main():
    with open("input22.txt", "r") as f:
        data = f.read().splitlines()
    
    numbers = [int(x) for x in data]

    silver = 0
    gold = 0

    final = []
    seq_bananas = {}
    for n in numbers:
        bananas = [n % 10]
        for i in range(2000): # Do the secret calculation
            x = 64*n
            n = x ^ n
            n = n % 16777216

            x = n // 32
            n = x ^ n
            n = n % 16777216

            x = 2048*n
            n = x ^ n
            n = n % 16777216

            bananas.append(n % 10)
        
        final.append(n)

        bananas2 = [0] + bananas[:-1]
        changes = [a_i - b_i for a_i, b_i in zip(bananas, bananas2)]
        
        # Get the first number of bananas for each sequence for the current buyer
        buyer_seqs = {}
        for i in range(1,len(changes)-3):
            seq = ",".join([str(x) for x in changes[i:i+4]])
            
            if seq not in buyer_seqs:
                buyer_seqs[seq] = bananas[i+3]

        # Add the bananas per sequence to the total for the different sequences
        for bs in buyer_seqs:
            if bs in seq_bananas:
                seq_bananas[bs] += buyer_seqs[bs]
            else:
                seq_bananas[bs] = buyer_seqs[bs]

    silver = sum(final)
    gold = max(seq_bananas.values())
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()