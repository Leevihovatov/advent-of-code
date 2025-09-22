import numpy as np
import math

def main():
    data = open("input11.txt","r",encoding="utf-8").read()
    monkeys = data.split("Monkey")
    del monkeys[0]
    m = len(monkeys)

    items = []
    operations = []
    tests = []
    trues = []
    falses = []

    inspected = np.zeros((1,m))

    for monkey in monkeys:
        things = monkey.splitlines()
        items.append(things[1].split()[2:])
        operations.append(things[2].split()[4:])
        tests.append(things[3].split()[-1])
        trues.append(things[4].split()[-1])
        falses.append(things[5].split()[-1])


    rounds = 20

    for i in range(1,rounds+1):
        if i % 5 == 0:
            print(i)
            print(items[0])
        for j in range(0,m):
            
            for k in range(0,len(items[j])):
                worryLevel = items[j][k]

                if isinstance(worryLevel, str):
                    worryLevel = int(worryLevel[0:2])

                #yeah
                if operations[j][0] == "+":
                    if operations[j][1] == "old":
                        worryLevel += worryLevel
                    else:
                        worryLevel += int(operations[j][1])
                if operations[j][0] == "*":
                    if operations[j][1] == "old":
                        worryLevel *= worryLevel
                    else:
                        worryLevel *= int(operations[j][1])

                worryLevel = math.floor(worryLevel/3)

                if (worryLevel % int(tests[j])) == 0:
                    items[int(trues[j])].append(worryLevel)
                else:
                    items[int(falses[j])].append(worryLevel)

                inspected[0][j] += 1

            items[j].clear()
    
    print(inspected)

main()