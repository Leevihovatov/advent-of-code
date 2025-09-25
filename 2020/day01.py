def main():
    with open("input01.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    data = [int(x) for x in data]
    n = len(data)

    for i, x in enumerate(data):
        first = x

        j = i+1

        while j < n:
            second = data[j]

            if first + second == 2020:
                silver = first * second

            k = j+1

            while k < n:
                third = data[k]
                if first + second + third == 2020:
                    gold = first * second * third

                k += 1

            j += 1

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()