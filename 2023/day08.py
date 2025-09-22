import re
import copy
def main():
    with open("input08.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 1

    # Change to use as indexes
    instructions = data[0].replace('L','0').replace('R','1')
    del(data[0:2])
    
    nodes = []
    LRs = []
    start_nodes = [] # Here all that end in A
    for line in data:
        line = re.sub(r'[\=,()]','',line).split()
        if line[0][-1] == 'A':
            start_nodes.append(line[0])
        nodes.append(line[0])
        LRs.append([line[1],line[2]])
    
    # Part 1
    current = 'AAA'
    found = False
    while not found:
        for i in instructions:
            i = int(i)
            silver += 1
            ind = nodes.index(current)
            current = LRs[ind][i]
            if current == 'ZZZ':
                found = True
                break
    
    ## Part 2
    # Checked before that every start node has exactly one goal node
    # and then it starts to loop that cycle. Every cycle is their own.
    # Solution: Find the number of steps for each cycle to reach the goal
    #           and find the smallest number divisible by the loops step numbers
    #           That second part took way too long to implement correctly :D
    
    # Apparently there is ready LCM function which could have done all this
    found_in = []
    for current in start_nodes:
        found = False
        step = 0
        while not found:
            for i in instructions:
                i = int(i)
                step += 1
                ind = nodes.index(current)
                current = LRs[ind][i]
                if current[-1] == 'Z':
                    found = True
                    found_in.append(step)
                    break   
    
    # Here I found about python shallow and deep copies
    found_in_orig = copy.deepcopy(found_in)
    bingo = False
    # Increase the smallest number by its original loops step number
    # until  we get to number that all are factor of. (all increased are same)
    # When two numbers are the same: remove other one and change the "original"
    # loop step number to that, because those two numbers will only match every that number of loops
    # So combine the loops until left with only one loop number
    while not bingo:
        ind = found_in.index(min(found_in))
        found_in[ind] = found_in[ind]+found_in_orig[ind]
        if len(set(found_in)) < len(found_in): # Check if we have same numbers         
            if len(set(found_in)) == 1:
                bingo = True
                gold = found_in[0]
            else:
                # Get the index of the second of the duplicates for removal
                duplicate = [idx for idx, item in enumerate(found_in) if item in found_in[:idx]]
                found_in_orig[ind] = found_in[ind]
                found_in.pop(duplicate[0])
                found_in_orig.pop(duplicate[0])

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()