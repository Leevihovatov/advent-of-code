totalScore = 0

file = open("input2.txt","r",encoding="utf-8").read()
file = file.replace("X","1")
file = file.replace("Y","2")
file = file.replace("Z","3")
file = file.replace("A","1")
file = file.replace("B","2")
file = file.replace("C","3")
file = file.splitlines()

for i in file:
    #print(i)
    opp = int(i[0])
    you = int(i[2])
    diff = you-opp
    #print(diff)
    totalScore += you
    if diff == 1 or diff == -2:
        totalScore += 6
    if diff == 0:
        totalScore += 3
print(totalScore)

totalScore = 0
for i in file:
    #print(i)
    opp = int(i[0])
    you = int(i[2])
    diff = you-opp
    #print(diff)
    if you == 1: #lose
        if opp == 1:
            totalScore += 3
        else:
            totalScore += (opp-1)
    if you == 2: #draw
        totalScore += (3+opp)
    if you == 3: #win
        if opp == 3:
            totalScore += (6+1)
        else:
            totalScore += (6+opp+1)
print(totalScore)