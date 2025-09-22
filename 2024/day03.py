import re

def main():
    with open("input03.txt", "r") as f:
        data = f.read()

    silver = 0
    gold = 0

    pattern = "mul\(.[0-9]*,.[0-9]*\)"
    valid = re.findall(pattern, data)
    valid = [[m.start(0), m.group()] for m in re.finditer(pattern, data)]

    enabling = [m.start(0) for m in re.finditer("do\(\)",data)]
    disabling = [m.start(0) for m in re.finditer("don\'t\(\)",data)]

    for v in valid:
        nums = v[1][4:-1].split(',')
        silver += int(nums[0])*int(nums[1])

    instructions_enabled = True
    for i in range(len(data)):
        if enabling[0] == i:
            instructions_enabled = True
            enabling.append(enabling.pop(0))
        elif disabling[0] == i:
            instructions_enabled = False
            disabling.append(disabling.pop(0))
        elif valid[0][0] == i:
            if instructions_enabled:
                nums = valid[0][1][4:-1].split(',')
                gold += int(nums[0])*int(nums[1])
            valid.append(valid.pop(0))
    

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()