def main():
    with open("input02.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    for report in data:
        r = [int(x) for x in report.split()]
 
        diff = []
        for i in range(len(r)-1):
            diff.append(r[i+1]-r[i])

        abs_diff = [abs(x) for x in diff]
        
        if max(abs_diff) < 4 and (max(diff) < 0 or min(diff) > 0):
            silver += 1
            gold += 1
        else:
            for i in range(len(r)):
                temp_r = r.copy()
                temp_r.pop(i)

                diff = []
                for j in range(len(temp_r)-1):
                    diff.append(temp_r[j+1]-temp_r[j])

                abs_diff = [abs(x) for x in diff]

                if max(abs_diff) < 4 and (max(diff) < 0 or min(diff) > 0):
                    gold += 1
                    break

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()