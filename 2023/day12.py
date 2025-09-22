from itertools import product, permutations
def main():
    with open("input12.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    for line in data:
        records = list(line.split()[0])
        truth = line.split()[1].split(',')
        truth = [int(x) for x in truth]
        known_springs = []
        all = []
        unknown_group = []
        l = 0
        s = 0
        """ for i,r in enumerate(records):
            if records[i] == '#':
                s += 1
            elif records[i] == '?':
                l += 1
            try:
                if records[i+1] != '#':
                    if s != 0:
                        unknown_group.append(s)
                        s = 0
                if records[i+1] != '?':
                    if l != 0:
                        unknown_group.append(-l)
                        l = 0
                if records[i+1] == '.':
                    if unknown_group:
                        all.append(unknown_group)
                        unknown_group = []
            except:
                if l != 0:
                    unknown_group.append(-l)
                elif s != 0:
                    unknown_group.append(s)
                if unknown_group:
                        all.append(unknown_group)
                        unknown_group = []
        unmapped = sum(truth)-sum(known_springs)
        
        if len(truth) == len(all):
            for i,t in enumerate(truth):
                print(sum(all[i])) """
        
        unknowns = []
        known_springs = 0
        for i,r in enumerate(records):
            if r == '?':
                unknowns.append(i)
            elif r == '#':
                known_springs += 1
                
        def find_groups(records):
            springs = []
            s = 0  
            for j,r in enumerate(records):
                if records[j] == '#':
                    s += 1
                try:
                    if records[j+1] == '.' and s != 0:
                        springs.append(s)
                        s = 0
                except:
                    if s != 0:
                        springs.append(s)
            return springs
        
        need_springs = sum(truth)-known_springs
        #print(need_springs)
        """ b0 = '1'*need_springs
        b0 += '0'*(len(unknowns)-need_springs)
        b1 = [int(x) for x in b0]
        binaries = list(set(list(permutations(b1)))) """
        #print(binaries[0])
        binaries = list(product([0, 1], repeat=len(unknowns)))
        
        #?###??????????###??????????###??????????###???????? 3,2,1,3,2,1,3,2,1,3,2,1,3,2,1
        possible = 0
        for binary in binaries:
            for i,b in enumerate(binary):
                if b == 0:
                    records[unknowns[i]] = '.'
                else:
                    records[unknowns[i]] = '#'
            guess = find_groups(records)
            if guess == truth:

                possible += 1
        silver += possible
        #print("".join(records))
        #print(possible)
        #print(f'true: {truth}')           
        #print(f'visible: {known_springs}')   
        #print(f'all: {all}')
        #print(f'unmapped: {unmapped}')
        #print('\n')
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()