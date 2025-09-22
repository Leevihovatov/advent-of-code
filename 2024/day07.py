def main():
    with open("input07.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    # Calculate binaries and ternaries beforehand
    binaries = []
    for i in range(2**(13-1)):
        binaries.append(bin(i)[2:])
    
    def ternary(n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))

    ternaries = []
    for i in range(3**(13-1)):
        ternaries.append(ternary(i))


    # Go through all possible combinations of operators
    # For combinations use binary/ternary

    def calc_silver(numbers, value):
        bins = binaries[:2**(len(numbers)-1)]
        bins = [b.zfill(len(numbers)-1) for b in bins]

        for bi in bins:
            result = numbers[0]
            for i, b in enumerate(bi):
                if b == '0':
                    result += numbers[i+1]
                else:
                    result *= numbers[i+1]

            if result == value:
                return value

        return 0
    
    def calc_gold(numbers, value):
        trns = ternaries[:3**(len(numbers)-1)]
        trns = [t.zfill(len(numbers)-1) for t in trns]

        for tr in trns:
            result = numbers[0]
            for i, t in enumerate(tr):
                if t == '0':
                    result += numbers[i+1]
                elif t == '1':
                    result *= numbers[i+1]
                else:
                    result = int(str(result)+str(numbers[i+1]))

            if result == value:
                return value

        return 0


    for equation in data:
        value = int(equation.split(':')[0])
        numbers = [int(x) for x in equation.split(':')[1].split()]

        silver += calc_silver(numbers, value)
        
        gold += calc_gold(numbers, value)


    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()