stacks = []
stacks.append(["C","F","B","L","D","P","Z","S"])
stacks.append(["B","W","H","P","G","V","N"])
stacks.append(["G","J","B","W","F"])
stacks.append(["S","C","W","L","F","N","J","G"])
stacks.append(["H","S","M","P","T","L","J","W"])
stacks.append(["S","F","G","W","C","B"])
stacks.append(["W","B","Q","M","P","T","H"])
stacks.append(["T","W","S","F"])
stacks.append(["R","C","N"])

orders = open("input5.txt","r",encoding="utf-8").read()
orders = orders.splitlines()

for o in orders:
    o2 = o.split()
    nro = int(o2[1])
    fs = int(o2[3])
    ts = int(o2[5])
    moved = stacks[fs-1][:nro]
    stacks[fs-1] = stacks[fs-1][nro:]
    #moved.reverse()
    #print(stacks[ts-1])
    newstack = stacks[ts-1]
    moved.extend(newstack)
    stacks[ts-1] = moved

finalstring = ""
for s in stacks:
    finalstring += s[0]
print(finalstring)